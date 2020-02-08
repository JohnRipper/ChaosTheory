
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Invite_Metadata(DiscordObject):
   uses: int = -1 # number of times this invite has been used
   max_uses: int = -1 # max number of times this invite can be used
   max_age: int = -1 # duration (in seconds) after which the invite expires
   temporary: bool = False # whether this invite only grants temporary membership
   created_at: Iso8601 timestamp # when this invite was created

