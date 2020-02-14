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

    #####
    # Client Control
    #####
    async def send_socket(self, data):
        await self._bot.send(message=data)


    #####
    # Api Commands
    #####
    async def send_message(self, message):
        # todo get message example
        data = {
            "d": message
        }
        await self._bot.send(data)