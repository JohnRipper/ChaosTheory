
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Integration_Account(DiscordObject):
   id: str = "" # id of the account
   name: str = "" # name of the account

