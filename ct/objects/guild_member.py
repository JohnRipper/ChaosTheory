from dataclasses import dataclass, field
from typing import Optional

from ct.objects.discord_object import DiscordObject
from ct.objects.user import User


@dataclass
class GuildMember(DiscordObject):
   deaf: bool  # whether the user is deafened in voice channels
   mute: bool  # whether the user is muted in voice channels
   user: User  # the user this guild member represents
   roles: [int]  # array of snowflakes
   hoisted_role: Optional[int] = field(default=None)
   nick: Optional[str] = field(default=None)  # this users guild nickname (if one is set)
   joined_at: str = ""  # when the user joined the guild
   premium_since: Optional[str] = field(default=None)  # when the user used their Nitro boost on the server
