
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

from ct.objects.snowflake import Snowflake


@dataclass
class MessageApplication(DiscordObject):
    id: Snowflake  # id of the application
    cover_image_: str = ""  # id of the embed's image asset
    description: str = ""  # application's description
    icon: str = ""  # id of the application's icon
    name: str = ""  # name of the application

