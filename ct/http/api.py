from ct.http.client import HttpClient
from ct.http.endpoint import Endpoint


class Api:
    def __init__(self, token: str):
        self._client = HttpClient(token=token)

    async def gateway(self):
        """
        /gateway
        Returns an object with a single valid WSS URL, which the client can use for Connecting.
        Clients should cache this value and only call this endpoint to retrieve a new URL if
        they are unable to properly establish a connection using the cached version of the URL.
        Example Response:
        {
            "url": "wss://gateway.discord.gg/"
        }
        """
        print(Endpoint.gateway)
        response = await self._client.get(url=Endpoint.gateway)
        return await response.text()

