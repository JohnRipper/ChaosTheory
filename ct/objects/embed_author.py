
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

@dataclass
class EmbedAuthor(DiscordObject):
    name_: str = ""  # name of author
    url_: str = ""  # url of author
    icon_url_: str = ""  # url of author icon (only supports http(s) and attachments)
    proxy_icon_url_: str = ""  # a proxied url of author icon

