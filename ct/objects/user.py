from dataclasses import dataclass
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class User(DiscordObject):
    id: int = 0  # the user's id
    username: str = ""  # the user's username, not unique across the platform
    discriminator: str = ""  # the user's 4-digit discord-tag
    avatar: str = ""  #
    bot: Optional[bool] = None  # whether the user belongs to an OAuth2 application
    system: Optional[bool] = None  # if the user is an Official Discord System user (part of the urgent message system)
    mfa_enabled: Optional[bool] = None  # whether the user has two factor enabled on their account
    locale: Optional[str] = None  # the user's chosen language option
    verified: Optional[bool] = None  # whether the email on this account has been verified
    email: Optional[str] = None  # the user's email
    flags: Optional[int] = None  #
    premium_type: Optional[int] = None  #
