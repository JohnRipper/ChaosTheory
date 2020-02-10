
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject
from ct.objects.snowflake import Snowflake


@dataclass
class Overwrite(DiscordObject):
   id: Snowflake  # role or user id
   type: str = ""  # either "role" or "member"
   allow: int = -1  # permission bit set
   deny: int = -1  # permission bit set

