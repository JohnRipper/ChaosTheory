import asyncio
import json
import random
import socket
import struct
from typing import List

import websockets
import youtube_dl
from websockets.protocol import State

from ct.cog.cog import Cog
from ct.cog.decorators import event
from ct.command import makeCommand, Command
from ct.objects.embed import Embed
from ct.objects.embed_field import EmbedField
from ct.objects.embed_footer import EmbedFooter
from ct.objects.message import Message
from ct.objects.presence import Presence
from ct.objects.user import User
from ct.objects.voice_ready import VoiceReady
from ct.objects.voice_server_update import VoiceServerUpdate
from ct.objects.voice_state import VoiceState

try:
    import nacl.secret

    has_nacl = True
except ImportError:
    has_nacl = False


class VoiceChannelHandler:
    supported_modes = (
        'xsalsa20_poly1305_lite',
        'xsalsa20_poly1305_suffix',
        'xsalsa20_poly1305',
    )

    def __init__(self, api):
        self.client: websockets.connect
        self.secret_key: List[int]
        self.media_session_id: str
        self.ssrc: int
        self.api = api
        self.sock: socket.socket

    def _encrypt_xsalsa20_poly1305(self, header, data):
        box = nacl.secret.SecretBox(bytes(self.secret_key))
        nonce = bytearray(24)
        nonce[:12] = header

        return header + box.encrypt(bytes(data), bytes(nonce)).ciphertext

    def _encrypt_xsalsa20_poly1305_suffix(self, header, data):
        box = nacl.secret.SecretBox(bytes(self.secret_key))
        nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)

        return header + box.encrypt(bytes(data), nonce).ciphertext + nonce

    def _encrypt_xsalsa20_poly1305_lite(self, header, data):
        box = nacl.secret.SecretBox(bytes(self.secret_key))
        nonce = bytearray(24)

        nonce[:4] = struct.pack('>I', self._lite_nonce)
        self.checked_add('_lite_nonce', 1, 4294967295)

        return header + box.encrypt(bytes(data), bytes(nonce)).ciphertext + nonce[:4]

    async def download_audio(self):

        ydl_opts = {'format': 'bestaudio/best',
                    'outtmpl': './tmp/%(id)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'opus',
                        'preferredquality': '192',
                    }]}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

    async def send_audio(self):
        with open("audio.opus", "r") as file:
            sequence = 0
            while binary_data := file.read(24):
                voice_packet = bytearray(24)
                struct.pack_into('>B', voice_packet, 0, 0x80)
                struct.pack_into('>B', voice_packet, 1, 0x79)
                struct.pack_into('>H', voice_packet, 2, sequence)
                struct.pack_into('>I', voice_packet, 4, timestamp)
                struct.pack_into('>I', voice_packet, 8, self.ssrc)
                struct.pack_into('>????', voice_packet, 12, binary_data)
                sequence += 1
                self.sock.sendto(voice_packet, (self.voice_server_ip, self.voice_server_port))

    async def connect(self, vsu: VoiceServerUpdate, session_id: str, user_id: str):
        async with websockets.connect(
                uri=f"wss://{vsu.endpoint.split(':')[0]}",
                timeout=60) as self.client:
            data = {
                "op": 0,
                "d": {
                    "server_id": str(vsu.guild_id),
                    "user_id": str(user_id),
                    "session_id": str(session_id),
                    "token": vsu.token
                }
            }
            await self.client.send(json.dumps(data))
            async for message in self.client:
                if message:
                    print(message)
                    await self.api.create_message(content=message, channel_id="363364911608496130")

                    if type(message) == str:
                        data = json.loads(message)
                        if data.get("op", False) == 8:
                            beat = data["d"]["heartbeat_interval"]
                            asyncio.create_task(self.heartbeat(beat))
                        if data.get("op", False) == 4:
                            self.secret_key = data["d"]["secret_key"]
                            self.media_session_id = data["d"]["media_session_id"]

                        if data.get("op", False) == 2:
                            vr = VoiceReady(**data["d"])
                            self.ssrc = vr.ssrc
                            self.sock = socket.socket(socket.AF_INET,  # Internet
                                                      socket.SOCK_DGRAM)  # UDP

                            self.sock.setblocking(False)

                            packet = bytearray(70)
                            struct.pack_into('>I', packet, 0, vr.ssrc)
                            self.sock.sendto(packet, (vr.ip, vr.port))
                            recv = await asyncio.get_event_loop().sock_recv(sock, 70)
                            print(recv)
                            ip = recv.replace(b"\x00", b"")[3:-2]
                            port = struct.unpack_from('>H', recv, len(recv) - 2)[0]

                            select_protocol_payload = {
                                "op": 1,
                                "d": {
                                    "protocol": "udp",
                                    "data": {
                                        "address": ip.decode(),
                                        "port": int(port),
                                        "mode": "xsalsa20_poly1305_lite"
                                    }
                                }
                            }
                            print(select_protocol_payload)
                            await self.client.send(json.dumps(select_protocol_payload))

    async def heartbeat(self, beat):
        if self.client.state == State.OPEN:
            data = {
                "op": 3,
                "d": random.randint(1000000000000, 9999999999999)
            }
            await self.client.send(json.dumps(data))
            # fuckin bad
            await asyncio.sleep(beat / 1000.0)
            asyncio.create_task(self.heartbeat(beat))


class Example(Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.voice_servers = {}

    @makeCommand(aliases=["join2"], description="<str> joins a room")
    async def join_this_channel(self, c: Command):
        print("joining chanel")
        await self.join_voice_channel("322640059935227906", "696864934109118516", False, False)
        #  {"t":"VOICE_SERVER_UPDATE","s":7,"op":0,"d":{"token":"b778c8ab48e14a94","guild_id":"322640059935227906","endpoint":"us-central372.discord.media:80"}}

    @makeCommand(aliases=["join"], description="<str> joins a room")
    async def join_channel(self, c: Command):
        print("joining chanel")
        await self.join_voice_channel("322640059935227906", "371291148209356811", False, False)
        #  {"t":"VOICE_SERVER_UPDATE","s":7,"op":0,"d":{"token":"b778c8ab48e14a94","guild_id":"322640059935227906","endpoint":"us-central372.discord.media:80"}}

    @event(event="VOICE_STATE_UPDATE")
    async def voice_state(self, vs: VoiceState):

        await self.api.create_message(content=vs, channel_id="363364911608496130")

    @event(event="VOICE_SERVER_UPDATE")
    async def voice_server_update(self, vsu: VoiceServerUpdate):
        await self.api.create_message(content=vsu, channel_id="363364911608496130")
        await self.connect_to_server(vsu)

    async def connect_to_server(self, vsu):
        if self.voice_servers.get(vsu.guild_id, False):
            # do something here
            return
        vch = VoiceChannelHandler(self.api)
        await vch.connect(vsu=vsu, session_id=self._bot.identity.session_id, user_id=self._bot.identity.user.id)
        self.voice_servers.update({vsu.guild_id: vch})

    @event(event="MESSAGE_UPDATE")
    async def message_change(self, message: Message):
        # {"t":"MESSAGE_UPDATE","s":20,"op":0,"d":
        # {"id":"693929708928237689","embeds":[{"type":"rich","title":"PRESENCE_UPDATE","footer":{"text":"at 1585516132370"},"description":"Sigma is now playing with milk","color":4053672}],"channel_id":"392823861349187584","guild_id":"322640059935227906"}}
        if message.author.id == '388147214448459779':
            return
        embed = Embed("")
        embed.title = "MESSAGE_UPDATE"
        embed.author = message.author
        embed.description = message.content
        embed.set_footer(text=f"{message.id}")

        if message.mentions:
            for mention in message.mentions:
                f = EmbedField()
                f.name = "hello world"
                f.value = mention.__repr__()
                embed.add_field(f)
        embed.color = 4053672
        await self.api.create_message(content="", channel_id="392823861349187584", embed=embed)

    @event(event="MESSAGE_CREATE")
    async def on_message(self, message: Message):
        if message.author.id == '388147214448459779':
            return
        embed = Embed("")
        embed.title = "MESSAGE_CREATE"
        embed.author = message.author
        embed.description = message.content
        embed.set_footer(text=f"{message.id}")

        if message.mentions:
            for mention in message.mentions:
                f = EmbedField()
                f.name = "hello world"
                f.value = mention.__repr__()
                embed.add_field(f)

        embed.color = 4053672
        await self.api.create_message(content="", channel_id="392823861349187584", embed=embed)

    @event(event="PRESENCE_UPDATE")
    async def on_presence(self, presence: Presence):
        embed = Embed("")
        embed.title = "PRESENCE_UPDATE"
        data = await self.api.get_user_from_id(presence.user.id)
        u = User(**data)

        if presence.status:
            embed.description = f"{u.username} is now {presence.status}"
        if presence.game:
            embed.description = f"{u.username} is now playing {presence.game.name}"

            embed.footer = EmbedFooter(text=f"at {presence.game.created_at}")
        embed.color = 4053672

        await self.api.create_message(content="", channel_id="392823861349187584", embed=embed)
