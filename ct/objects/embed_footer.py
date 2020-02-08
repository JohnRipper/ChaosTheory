
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Embed_Footer(DiscordObject):
   text: str = "" # footer text
   icon_url_: str = "" # url of footer icon (only supports http(s) and attachments)
   proxy_icon_url_: str = "" # a proxied url of footer icon

