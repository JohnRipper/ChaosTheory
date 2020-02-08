
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Guild_Embed(DiscordObject):
   enabled: bool = False # whether the embed is enabled
   channel_id: Snowflake # the embed channel id

