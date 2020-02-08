
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Reaction(DiscordObject):
   count: int = -1 # times this emoji has been used to react
   me: bool = False # whether the current user reacted using this emoji
   emoji:   # emoji information

