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
        self.api = self._bot.http

    #####
    # Client Control
    #####
    async def send_socket(self, data):
        await self._bot.send(message=data)


    #####
    # Api Commands
    #####
