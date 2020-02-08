
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Embed_Image(DiscordObject):
   url_: str = "" # source url of image (only supports http(s) and attachments)
   proxy_url_: str = "" # a proxied url of the image
   height_: int = -1 # height of image
   width_: int = -1 # width of image

