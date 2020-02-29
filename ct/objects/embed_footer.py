from dataclasses import dataclass, field
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class EmbedFooter(DiscordObject):
    text: str  # footer text
    icon_url: Optional[str] = field(default=None)  # url of footer icon (only supports http(s) and attachments)
    proxy_icon_url: Optional[str] = field(default=None)  # a proxied url of footer icon
