from dataclasses import dataclass, field
from typing import List, Optional

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
    footer: Optional[EmbedFooter] = field(default=None)  # footer information
    image: Optional[EmbedImage] = field(default=None)  # image information
    thumbnail: Optional[EmbedThumbnail] = field(default=None)  # thumbnail information
    video: Optional[EmbedVideo] = field(default=None)  # video information
    provider: Optional[EmbedProvider] = field(default=None)  # provider information
    author: Optional[EmbedAuthor] = field(default=None)  # author information
    fields: List[EmbedField] = field(default_factory=list)  # fields information

    title: Optional[str] = field(default=None)  # title of embed
    type: Optional[str] = field(default=None)  # type of embed (always "rich" for webhook embeds)
    description: Optional[str] = field(default=None)  # description of embed
    url: Optional[str] = field(default=None)  # url of embed
    timestamp: Optional[str] = field(default=None)  # timestamp of embed content
    color: Optional[int] = field(default=None)  # color code of the embed

    def set_footer(self, text: str, icon_url: str = None, proxy_icon_url: str = None):
        self.footer = EmbedFooter(text=text, icon_url=icon_url, proxy_icon_url=proxy_icon_url)

    def set_image(self, url: str = None, proxy_url: str = None, height: int = None, width: int = None):
        self.image = EmbedImage(url=url, proxy_url=proxy_url, height=height, width=width)

    def set_thumbnail(self, url: str = None, proxy_url: str = None, height: int = None, width: int = None):
        self.thumbnail = EmbedThumbnail(url=url, proxy_url=proxy_url, height=height, width=width)

    def set_video(self, url: str = None, height: int = None, width: int = None):
        self.video = EmbedVideo(url=url, height=height, width=width)

    def set_provider(self, name: str = None, url: str = None):
        self.provider = EmbedProvider(name=name, url=url)

    def set_author(self, name: str = None, url: str = None, icon_url: str = None, proxy_icon_url: str = None):
        self.author = EmbedAuthor(name=name, url=url, icon_url=icon_url, proxy_icon_url=proxy_icon_url)

    def add_field(self, embed_field: EmbedField):
        # todo, validate data?
        self.fields.append(embed_field)
