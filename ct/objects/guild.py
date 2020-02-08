
from dataclasses import dataclass

from ct.objects.channel import Channel
from ct.objects.discord_object import DiscordObject
from ct.objects.emoji import Emoji
from ct.objects.guild_member import GuildMember
from ct.objects.role import Role

from ct.objects.snowflake import Snowflake
from ct.objects.voice_state import VoiceState


@dataclass
class Guild(DiscordObject):
   id: Snowflake # guild id

   owner_id: Snowflake # id of owner
   rules_channel_id: Snowflake # the id of the channel in which a discoverable server's rules should be found
   afk_channel_id: Snowflake # id of afk channel
   application_id: Snowflake # application id of the guild creator if it is bot-created
   widget_channel_id_: Snowflake # the channel id for the server widget
   system_channel_id: Snowflake # the id of the channel to which system messages are sent
   roles: [Role] # roles in the guild
   emojis: [Emoji] # custom guild emojis
   embed_channel_id_: Snowflake # if not null, the channel id that the widget will generate an invite to
   voice_states_: [VoiceState]  #
   members_: [GuildMember]  # users in the guild
   channels_: [Channel]  # channels in the guild
   presences_: [Presence]  # presences of the users in the guild

   features: [GuildFeatures]    # enabled guild features
   joined_at_: str = "" # when this guild was joined at

   name: str = "" # guild name (2-100 characters)
   icon: str = "" # icon hash
   splash: str = "" # splash hash
   discovery_splash: str = "" # discovery splash hash
   owner_: bool = False #  
   permissions_: int = -1 #
   region: str = "" #  
   afk_timeout: int = -1 # afk timeout in seconds
   embed_enabled_: bool = False # whether this guild is embeddable (e.g. widget)
   verification_level: int = -1 #
   default_message_notifications: int = -1 #  
   explicit_content_filter: int = -1 # explicit content filter level

   mfa_level: int = -1 #  
   widget_enabled_: bool = False # whether or not the server widget is enabled

   system_channel_flags: int = -1 # system channel flags

   large_: bool = False # whether this is considered a large guild
   unavailable_: bool = False # whether this guild is unavailable
   member_count_: int = -1 # total number of members in this guild

   max_presences_: int = -1 # the maximum amount of presences for the guild (the default value, currently 5000, is in effect when null is returned)
   max_members_: int = -1 # the maximum amount of members for the guild
   vanity_url_code: str = "" # the vanity url code for the guild
   description: str = "" # the description for the guild
   banner: str = "" # banner hash
   premium_tier: int = -1 # premium tier
   premium_subscription_count_: int = -1 # the total number of users currently boosting this server
   preferred_locale: str = "" # the preferred locale of this guild only set if guild has the "DISCOVERABLE" feature, defaults to en-US


