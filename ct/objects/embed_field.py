
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

@dataclass
class EmbedField(DiscordObject):
    name: str = ""  # name of the field
    value: str = ""  # value of the field
    inline_: bool = False  # whether or not this field should display inline

