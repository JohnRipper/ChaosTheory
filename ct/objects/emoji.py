from dataclasses import dataclass, field
from typing import List, Optional

from ct.objects.discord_object import DiscordObject
from ct.objects.role import Role
from ct.objects.user import User


@dataclass
class Emoji(DiscordObject):
    id: int  # emoji id
    name: str  # (can be null only in reaction emoji objects) # emoji name
    roles: List[Role]  # roles this emoji is whitelisted to

    user: Optional[User] = field(default=None)  # user that created this emoji
    managed: Optional[bool] = field(default=None)  # user that created this emoji
    animated: Optional[bool] = field(default=None)  # user that created this emoji
    require_colons: Optional[bool] = field(default=None)  # user that created this emoji
