
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Integration(DiscordObject):
   id: Snowflake # integration id
   name: str = "" # integration name
   type: str = "" # integration type (twitch, youtube, etc)
   enabled: bool = False # is this integration enabled
   syncing: bool = False # is this integration syncing
   role_id: Snowflake # id that this integration uses for "subscribers"
   expire_behavior: int = -1 # the behavior of expiring subscribers
   expire_grace_period: int = -1 # the grace period before expiring subscribers
   user:   # user for this integration
   account:   # integration account information
   synced_at: Iso8601 timestamp # when this integration was last synced

