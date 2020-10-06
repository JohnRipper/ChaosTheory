
from dataclasses import dataclass

from ct.objects.discord_object import DiscordObject
from ct.objects.guild_member import GuildMember
from ct.objects.snowflake import Snowflake


@dataclass
class VoiceState(DiscordObject):
   guild_id: Snowflake  # the guild id this voice state is for
   channel_id: Snowflake  # the channel id this user is connected to
   user_id: Snowflake  # the user id this voice state is for
   member: GuildMember  # the guild member this voice state is for
   session_id: str = ""  # the session id for this voice state
   deaf: bool = False  # whether this user is deafened by the server
   mute: bool = False  # whether this user is muted by the server
   self_deaf: bool = False  # whether this user is locally deafened
   self_mute: bool = False  # whether this user is locally muted
   self_stream: bool = False  # whether this user is streaming using "Go Live"
   self_video: bool = False  # whether this user is streaming using "Go Live"
   suppress: bool = False  # whether this user is muted by the current user
