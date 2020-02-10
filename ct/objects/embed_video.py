
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

@dataclass
class EmbedVideo(DiscordObject):
    url_: str = ""  # source url of video
    height_: int = -1  # height of video
    width_: int = -1  # width of video

