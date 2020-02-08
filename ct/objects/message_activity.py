
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Message_Activity(DiscordObject):
   type: int = -1 # type of message activity
   party_id_: str = "" #  

