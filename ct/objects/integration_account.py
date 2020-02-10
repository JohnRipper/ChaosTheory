
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

@dataclass
class IntegrationAccount(DiscordObject):
   id: str = "" # id of the account
   name: str = "" # name of the account

