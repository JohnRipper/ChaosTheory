import ast
import asyncio
import json

import websockets

from ct.objects.payload import OpCode, Identity
from ct.http.api import Api
from ct.objects.api import Gateway

class Client:
    def __init__(self, token):
        self._client = None
        self.http = Api(token=token)
        self.token = token
        self.interval = 0

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
            await asyncio.sleep(self.interval)
            asyncio.create_task(self.heartbeat())
        else:
            raise Exception("heart beat interval wtf")

    async def _recv(self, message: str):
        message = json.loads(message)
        print(f"recv:{message}")
        if op:= message.get('op', False):
            if op == OpCode.Hello.value:
                self.interval = message['d'].get('heartbeat_interval', 0)
                asyncio.create_task(self.heartbeat())
                await self.send(Identity(self.token).__discord__())

            if op == OpCode.Dispatch.value:
                # todo , do this in a cog manager
                if event:= message.get('t', False):
                    routes = {
                        "READY": ("t", "b"),
                        "GUILD_CREATE": ("t", "b")
                    }
                    test = routes.get(event, None)

                    pass

    async def send(self, message: str = None, data: dict = None):
        if message:
            print(f"send:{message}")
            await self._client.send(message)
        if data:
            print(f"send:{data}")
            await self._client.send(json.dumps(message))





