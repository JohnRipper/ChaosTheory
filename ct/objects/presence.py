from dataclasses import dataclass, field
from typing import List, Optional

from ct.objects.activity import Activity
from ct.objects.client_status import ClientStatus
from ct.objects.discord_object import DiscordObject
from ct.objects.role import Role
from ct.objects.snowflake import Snowflake
from ct.objects.user import User


@dataclass
class Presence(DiscordObject):
    roles: [Role]  # roles this user is in
    game: Activity  # null, or the user's current activity
    guild_id: Snowflake  # id of the guild
    activities: List[Activity]  # user's current activities
    client_status: ClientStatus  # user's platform-dependent status
    status: str  # either "idle", "dnd", "online", or "offline"\
    user: User  # the user presence is being updated for
    premium_since: Optional[str] = field(default=None)  # when the user used their Nitro boost on the server
    nick: Optional[str] = field(default=None)  # this users guild nickname (if one is set)
