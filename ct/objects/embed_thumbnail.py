from dataclasses import dataclass, field
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class EmbedThumbnail(DiscordObject):
    url: Optional[str] = field(default=None)  # source url of thumbnail (only supports http(s) and attachments)
    proxy_url: Optional[str] = field(default=None)  # a proxied url of the thumbnail
    height: Optional[int] = field(default=None)  # height of thumbnail
    width: Optional[int] = field(default=None)  # width of thumbnail
