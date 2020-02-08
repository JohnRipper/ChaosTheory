import ast
import asyncio
import json

import websockets

from ct.cog.cog_manager import CogManager
from ct.objects.payload import OpCode, Identity
from ct.http.api import Api
from ct.objects.api import Gateway

class Client:
    def __init__(self, token):
        self._client = None
        self.http = Api(token=token)
        self.token = token
        self.interval = 0
        self.sequence = 0
        self.cm = CogManager()

    async def connect(self):
        # get a valid websocket url from discord
        gateway_data = ast.literal_eval(await self.http.gateway())
        g = Gateway(**gateway_data)

        async with websockets.connect(
            uri=g.url,
            timeout=60) as self._client:
            async for message in self._client:
                await self._recv(message=message)

    async def heartbeat(self):
        if self.interval != 0:

            await self.send(json.dumps({
                    "op": 1,
                    "d": self.sequence
                }))
            await asyncio.sleep(self.interval / 1000.0)

            asyncio.create_task(self.heartbeat())
        else:
            raise Exception("heart beat interval wtf")

    async def _recv(self, message: str):
        message = json.loads(message)
        print(f"recv:{message}")
        op = message.get('op', -1)
        if op != -1:
            self.sequence = message.get("s", None)
            print(f"s:{self.sequence}")

            if op == OpCode.Hello.value:
                self.interval = message['d'].get('heartbeat_interval', 0)
                asyncio.create_task(self.heartbeat())
                await self.send(Identity(self.token).__discord__())

            if op == OpCode.Dispatch.value:
                self.cm.do_event(event=message.get('t', False), data=message)
                # todo create a command router in cog manager.

            if op == OpCode.InvalidSession.value:
                # todo custom exceptions
                print("Invalid session, disconnecting. ")

    async def send(self, message: str = None):
        print(f"send:{message}")

        if type(message) is str:
            await self._client.send(message)

        if type(message) is dict:
            await self._client.send(json.dumps(message))





