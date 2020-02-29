from ct.cog.cog import Cog
from ct.cog.decorators import event
from ct.objects.embed import Embed
from ct.objects.message import Message
from ct.objects.presence import Presence


class Example(Cog):

    @event(event="MESSAGE_CREATE")
    async def on_message(self, message: Message):

        if message.content.startswith("#test"):
            print(message.content)
            if message.mentions:
                print(message.mentions)
        pass

    @event(event="PRESENCE_UPDATE")
    async def on_presence(self, presence: Presence):
        print(presence.status)
        print(presence.user.id)
        embed = Embed()
        await self.api.create_message(content=presence.__repr__(), channel_id="392823861349187584", embed=embed)
