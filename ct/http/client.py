from aiohttp import ClientSession, ClientResponse


class HttpClient:
    def __init__(self, token):
        self._session = ClientSession()
        self._auth = {
            'Authorization': f'Bot {token}'
        }

    async def get(self, url: str) -> ClientResponse:
        return await self._session.get(url=url)

    async def post(self, url: str) -> ClientResponse:
        return await self._session.post(url=url, headers=self._auth)