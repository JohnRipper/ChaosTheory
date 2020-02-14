from ct.cog.cog import Cog
from ct.cog.decorators import event
from ct.objects.message import Message
from ct.objects.presence import Presence


class Example(Cog):

    @event(event="MESSAGE_CREATE")
    async def on_message(self, message: Message):
        print(message)

        if message.content.startswith("#test"):
            print(message.content)
            if message.mentions:
                print(message.mentions)
        pass


    @event(event="PRESENCE_UPDATE")
    async def on_presence(self, presence: Presence):
        print(presence.status)
        print(presence.__repr__())
