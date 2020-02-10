
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

from ct.objects.emoji import Emoji


@dataclass
class Reaction(DiscordObject):
   emoji: Emoji  # emoji information

   count: int = -1 # times this emoji has been used to react
   me: bool = False # whether the current user reacted using this emoji

