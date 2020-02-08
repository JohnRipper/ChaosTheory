
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Embed_Thumbnail(DiscordObject):
   url_: str = "" # source url of thumbnail (only supports http(s) and attachments)
   proxy_url_: str = "" # a proxied url of the thumbnail
   height_: int = -1 # height of thumbnail
   width_: int = -1 # width of thumbnail

