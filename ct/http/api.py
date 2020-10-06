import json

from ct.http.client import HttpClient
from ct.http.endpoint import Endpoint
from ct.logger import ChaosLogger
from ct.objects.embed import Embed


class Api:
    def __init__(self, token: str):
        self.__client = HttpClient(token=token)
        self.ep = Endpoint()
        self.log = ChaosLogger("Api")


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
        response = await self.__client.get(url=Endpoint.gateway)
        return await response.text()

    async def create_message(self, channel_id: int, content: str, tts=False, embed: Embed = None):

        url = Endpoint.BASE + f"/channels/{channel_id}/messages"
        data = {"content": str(content)}
        if embed:
            embed_dict = embed.to_dict()
            data.update({"embed": embed_dict})
        result = await self.__client.post(url, {"payload_json": json.dumps(data)})

    async def get_user_from_id(self, user_id: int):
        url = self.ep.users(user_id=user_id)
        result = await self.__client.get(url)
        result = await result.json()
        if 'message' in result:
            self.log.warning(f'get_user_from_id error : {result.get("message")}')
        return result
