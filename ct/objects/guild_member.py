
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject
from ct.objects.snowflake import Snowflake

from ct.objects.user import User


@dataclass
class GuildMember(DiscordObject):
   user: User  # the user this guild member represents
   roles: [Snowflake]  # array of snowflakes
   nick_: str = ""  # this users guild nickname (if one is set)
   joined_at: str = ""  # when the user joined the guild
   premium_since_: str = ""  # when the user used their Nitro boost on the server
   deaf: bool = False  # whether the user is deafened in voice channels
   mute: bool = False  # whether the user is muted in voice channels

