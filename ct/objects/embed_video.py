from dataclasses import dataclass, field
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class EmbedVideo(DiscordObject):
    url: Optional[str] = field(default=None)  # source url of video
    height: Optional[int] = field(default=None)  # height of video
    width: Optional[int] = field(default=None)  # width of video
