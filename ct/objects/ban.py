
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

from ct.objects.user import User


@dataclass
class Ban(DiscordObject):
   user: User  # the banned user
   reason: str = ""  # the reason for the ban

