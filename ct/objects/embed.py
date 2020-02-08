
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Embed(DiscordObject):
   title_: str = "" # title of embed
   type_: str = "" # type of embed (always "rich" for webhook embeds)
   description_: str = "" # description of embed
   url_: str = "" # url of embed
   timestamp_: Iso8601 timestamp # timestamp of embed content
   color_: int = -1 # color code of the embed
   footer_:   # footer information
   image_:   # image information
   thumbnail_:   # thumbnail information
   video_:   # video information
   provider_:   # provider information
   author_:   # author information
   fields_:   # fields information

