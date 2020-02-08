
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Channel_Mention(DiscordObject):
   id: Snowflake # id of the channel
   guild_id: Snowflake # id of the guild containing the channel
   type: int = -1 #  
   name: str = "" # the name of the channel

