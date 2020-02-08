
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Embed_Provider(DiscordObject):
   name_: str = "" # name of provider
   url_: str = "" # url of provider

