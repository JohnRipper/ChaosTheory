from dataclasses import dataclass, field
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class EmbedProvider(DiscordObject):
    name: Optional[str] = field(default=None)  # name of provider
    url: Optional[str] = field(default=None)  # url of provider
