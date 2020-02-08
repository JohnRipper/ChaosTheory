
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Message_Reference(DiscordObject):
   message_id_: Snowflake # id of the originating message
   channel_id: Snowflake # id of the originating message's channel
   guild_id_: Snowflake # id of the originating message's guild

