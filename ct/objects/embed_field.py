
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Embed_Field(DiscordObject):
   name: str = "" # name of the field
   value: str = "" # value of the field
   inline_: bool = False # whether or not this field should display inline

