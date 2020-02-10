
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

from ct.objects.snowflake import Snowflake


@dataclass
class Attachment(DiscordObject):
    id: Snowflake  # attachment id
    filename: str = ""  # name of file attached
    size: int = -1  # size of file in bytes
    url: str = ""  # source url of file
    proxy_url: str = ""  # a proxied url of file
    height: int = -1  # height of file (if image)
    width: int = -1  # width of file (if image)

