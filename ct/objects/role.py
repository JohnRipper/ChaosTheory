
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject
from ct.objects.snowflake import Snowflake


@dataclass
class Role(DiscordObject):
    id: Snowflake  # the role's id
    name: str = ""  # role name
    color: int = -1  # integer representation of a hexadecimal color code
    hoist: bool = False  # if this role is pinned in the user listing
    position: int = -1  # position of this role
    permissions: int = -1  # permission bit set
    managed: bool = False  # wether this role is managed by integration
    mentionable: bool = False  # wether this role is mentionable



