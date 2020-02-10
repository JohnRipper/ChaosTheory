
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

@dataclass
class EmbedFooter(DiscordObject):
    text: str = ""  # footer text
    icon_url_: str = ""  # url of footer icon (only supports http(s) and attachments)
    proxy_icon_url_: str = ""  # a proxied url of footer icon

