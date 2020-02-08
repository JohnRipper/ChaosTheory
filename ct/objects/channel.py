
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Channel(DiscordObject):
   id: Snowflake # the id of this channel
   type: int = -1 #  
   guild_id_: Snowflake # the id of the guild
   position_: int = -1 # sorting position of the channel
   permission_overwrites_:   # explicit permission overwrites for members and roles
   name_: str = "" # the name of the channel (2-100 characters)
   topic_: str = "" # the channel topic (0-1024 characters)
   nsfw_: bool = False # whether the channel is nsfw
   last_message_id_: Snowflake # the id of the last message sent in this channel (may not point to an existing or valid message)
   bitrate_: int = -1 # the bitrate (in bits) of the voice channel
   user_limit_: int = -1 # the user limit of the voice channel
   rate_limit_per_user_: int = -1 #  
   recipients_:   # the recipients of the DM
   icon_: str = "" # icon hash
   owner_id_: Snowflake # id of the DM creator
   application_id_: Snowflake # application id of the group DM creator if it is bot-created
   parent_id_: Snowflake # id of the parent category for a channel (each parent category can contain up to 50 channels)
   last_pin_timestamp_: Iso8601 timestamp # when the last pinned message was pinned

