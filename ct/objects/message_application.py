from dataclasses import dataclass, field
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class MessageApplication(DiscordObject):
    id: int  # id of the application
    description: str  # application's description
    icon: str  # id of the application's icon
    name: str  # name of the application
    cover_image: Optional[str] = field(default=None)  # id of the embed's image asset
