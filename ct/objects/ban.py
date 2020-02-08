
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Ban(DiscordObject):
   reason: str = "" # the reason for the ban
   user:   # the banned user

