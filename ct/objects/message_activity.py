
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

@dataclass
class MessageActivity(DiscordObject):
   type: int = -1 # type of message activity
   party_id_: str = "" #  

