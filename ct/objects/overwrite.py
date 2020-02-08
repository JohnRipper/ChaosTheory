
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Overwrite(DiscordObject):
   id: Snowflake # role or user id
   type: str = "" # either "role" or "member"
   allow: int = -1 # permission bit set
   deny: int = -1 # permission bit set

