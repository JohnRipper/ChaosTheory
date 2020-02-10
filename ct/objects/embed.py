
from dataclasses import dataclass
from typing import List

from ct.objects.discord_object import DiscordObject

from ct.objects.embed_author import EmbedAuthor
from ct.objects.embed_field import EmbedField
from ct.objects.embed_footer import EmbedFooter
from ct.objects.embed_image import EmbedImage
from ct.objects.embed_provider import EmbedProvider
from ct.objects.embed_thumbnail import EmbedThumbnail
from ct.objects.embed_video import EmbedVideo




@dataclass
class Embed(DiscordObject):
    footer_: EmbedFooter  # footer information
    image_: EmbedImage  # image information
    thumbnail_: EmbedThumbnail  # thumbnail information
    video_: EmbedVideo  # video information
    provider_: EmbedProvider  # provider information
    author_: EmbedAuthor  # author information
    fields_: List[EmbedField]  # fields information

    title_: str = ""  # title of embed
    type_: str = ""  # type of embed (always "rich" for webhook embeds)
    description_: str = ""  # description of embed
    url_: str = ""  # url of embed
    timestamp_: str = ""  # timestamp of embed content
    color_: int = -1  # color code of the embed


