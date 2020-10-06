from dataclasses import dataclass

from ct.objects.discord_object import DiscordObject
from ct.objects.snowflake import Snowflake


@dataclass
class Webhook(DiscordObject):
    id: Snowflake  # the id of the webhook
    type: int = -1  #
    guild_id_: Snowflake  # the guild id this webhook is for
    channel_id: Snowflake  # the channel id this webhook is for
    user_:  # the user this webhook was created by (not returned when getting a webhook with its token)
    name: str = ""  # the default name of the webhook
   avatar: str = "" # the default avatar of the webhook
   token_: str = "" # the secure token of the webhook (returned for Incoming Webhooks)

