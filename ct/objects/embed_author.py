from dataclasses import dataclass
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class EmbedAuthor(DiscordObject):
    name: Optional[str] = ""  # name of author
    url: Optional[str] = ""  # url of author
    icon_url: Optional[str] = ""  # url of author icon (only supports http(s) and attachments)
    proxy_icon_url: Optional[str] = ""  # a proxied url of author icon
