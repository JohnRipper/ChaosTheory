from dataclasses import dataclass, field
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class EmbedImage(DiscordObject):
    url: Optional[str] = field(default=None)  # source url of image (only supports http(s) and attachments)
    proxy_url: Optional[str] = field(default=None)  # a proxied url of the image
    height: Optional[int] = field(default=None)  # height of image
    width: Optional[int] = field(default=None)  # width of image
