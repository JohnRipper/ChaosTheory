
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Emoji(DiscordObject):
   id: Snowflake # emoji id
   name: String (can be null only in reaction emoji objects) # emoji name
   roles_:   # roles this emoji is whitelisted to
   user_:   # user that created this emoji
   require_colons_: bool = False # whether this emoji must be wrapped in colons
   managed_: bool = False # whether this emoji is managed
   animated_: bool = False # whether this emoji is animated

