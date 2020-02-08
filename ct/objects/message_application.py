
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Message_Application(DiscordObject):
   id: Snowflake # id of the application
   cover_image_: str = "" # id of the embed's image asset
   description: str = "" # application's description
   icon: str = "" # id of the application's icon
   name: str = "" # name of the application

