
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject
from ct.objects.snowflake import Snowflake


@dataclass
class User(DiscordObject):
   id: Snowflake # the user's id
   username: str = "" # the user's username, not unique across the platform
   discriminator: str = "" # the user's 4-digit discord-tag
   avatar: str = "" #  
   bot_: bool = False # whether the user belongs to an OAuth2 application
   system_: bool = False # whether the user is an Official Discord System user (part of the urgent message system)
   mfa_enabled_: bool = False # whether the user has two factor enabled on their account
   locale_: str = "" # the user's chosen language option
   verified_: bool = False # whether the email on this account has been verified
   email_: str = "" # the user's email
   flags_: int = -1 #  
   premium_type_: int = -1 #  

