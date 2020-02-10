
from dataclasses import dataclass, fields, field
from typing import List

from ct.objects.discord_object import DiscordObject

from ct.objects.role import Role
from ct.objects.snowflake import Snowflake
from ct.objects.user import User


@dataclass
class Emoji(DiscordObject):
    id: Snowflake  # emoji id
    user_: User  # user that created this emoji
    name: str  # (can be null only in reaction emoji objects) # emoji name
    roles_: List[Role]  # roles this emoji is whitelisted to
    require_colons_: bool = False  # whether this emoji must be wrapped in colons
    managed_: bool = False  # whether this emoji is managed
    animated_: bool = False  # whether this emoji is animated

