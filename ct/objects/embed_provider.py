
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

@dataclass
class EmbedProvider(DiscordObject):
    name_: str = ""  # name of provider
    url_: str = ""  # url of provider

