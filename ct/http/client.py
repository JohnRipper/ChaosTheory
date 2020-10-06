import asyncio
import time

from aiohttp import ClientSession, ClientResponse, TCPConnector


class HttpClient:

    def __init__(self, token):
        conn = TCPConnector(limit=1)

        self._session = ClientSession(connector=conn)
        self._token = token
        self._auth = {
            'Authorization': f'Bot {token}',
            'Content-Type': 'application/x-www-form-urlencoded'

        }
        self.requests = []

    @property
    async def get_header(self):
        return {
            'Authorization': f'Bot {self._token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    async def get(self, url: str) -> ClientResponse:
        initial = time.time()
        while True:
            await asyncio.sleep(1.2)
            if time.time() - initial > 1:
                return await self._session.get(url=url, headers=self._auth)

    async def post(self, url: str, data: dict) -> ClientResponse:
        initial = time.time()
        while True:
            await asyncio.sleep(1.2)
            if time.time() - initial > 1:
                return await self._session.post(url=url, headers=self._auth, data=data)
