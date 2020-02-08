
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Embed_Video(DiscordObject):
   url_: str = "" # source url of video
   height_: int = -1 # height of video
   width_: int = -1 # width of video

