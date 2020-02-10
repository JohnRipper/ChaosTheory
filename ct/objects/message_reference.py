
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

from ct.objects.snowflake import Snowflake


@dataclass
class MessageReference(DiscordObject):
    message_id_: Snowflake  # id of the originating message
    channel_id: Snowflake  # id of the originating message's channel
    guild_id_: Snowflake  # id of the originating message's guild

