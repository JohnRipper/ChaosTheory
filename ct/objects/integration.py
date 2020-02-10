
from dataclasses import dataclass
from typing import List
from ct.objects.discord_object import DiscordObject
from ct.objects.integration_account import IntegrationAccount
from ct.objects.snowflake import Snowflake
from ct.objects.user import User


@dataclass
class Integration(DiscordObject):
   id: Snowflake  # integration id
   user: User  # user for this integration
   account: IntegrationAccount  # integration account information
   role_id: Snowflake  # id that this integration uses for "subscribers"
   synced_at: str  # when this integration was last synced
   name: str = ""  # integration name
   type: str = ""  # integration type (twitch, youtube, etc)
   enabled: bool = False  # is this integration enabled
   syncing: bool = False  # is this integration syncing
   expire_behavior: int = -1  # the behavior of expiring subscribers
   expire_grace_period: int = -1  # the grace period before expiring subscribers


