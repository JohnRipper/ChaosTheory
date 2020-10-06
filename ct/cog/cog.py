class Cog:
    def __init__(self, bot):
        self.name = self.__class__.__name__
        self.__cog__ = True
        self._bot = bot
        # check yourself before you wreck yourself.
        self.events = [getattr(self, name)
                       for name in dir(self)
                       if "__" not in name
                       and hasattr(getattr(self, name), "__event__")]

        self.commands = [getattr(self, name)
                         for name in dir(self)
                         if "__" not in name
                         and hasattr(getattr(self, name), "__command__")]

        self.api = self._bot.http

    #####
    # Client Control
    #####
    async def send_socket(self, data):
        await self._bot.send(message=data)

    async def send_message(self, data):
        await self._bot.send(message=data)

    async def join_voice_channel(self, guild_id: str, channel_id: str, self_mute: bool = False,
                                 self_deaf: bool = False):
        data = {
            "op": 4,
            "s": self._bot.sequence,
            "t": None,
            "d": {
                "guild_id": guild_id,
                "channel_id": channel_id,
                "self_mute": self_mute,
                "self_deaf": self_deaf
            }
        }
        await self.send_message(data)

    #####
    # Api Commands
    #####
