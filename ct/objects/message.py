
from dataclasses import dataclass
from typing import List, Union, Optional

from ct.objects.discord_object import DiscordObject

from ct.objects.attachment import Attachment
from ct.objects.channel import Channel
from ct.objects.embed import Embed
from ct.objects.guild_member import GuildMember
from ct.objects.message_activity import MessageActivity
from ct.objects.message_application import MessageApplication
from ct.objects.message_reference import MessageReference
from ct.objects.reaction import Reaction
from ct.objects.role import Role
from ct.objects.snowflake import Snowflake
from ct.objects.user import User




@dataclass
class Message(DiscordObject):
    id: Snowflake # id of the message
    channel_id: Snowflake  # id of the channel the message was sent in
    author: User  # the author of this message (not guaranteed to be a valid user)
    mentions: List[User]  # users specifically mentioned in the message |array of user objects, with an additional partial member field
    mention_roles: List[Role]  # roles specifically mentioned in this message
    mention_channels: List[Channel]  # channels specifically mentioned in this message
    attachments: List[Attachment]  # any attached files
    embeds: List[Embed]  # any embedded content
    reactions: List[Reaction]  # reactions to the message
    timestamp: str  # when this message was sent
    edited_timestamp: str  # when this message was edited (or null if never)
    content: str = ""  # contents of the message
    tts: bool = False  # whether this was a TTS message
    mention_everyone: bool = False # whether this message mentions everyone
    webhook_id: Optional[Snowflake] = None  # if the message is generated by a webhook, this is the webhook's id
    nonce: Optional[str] = None  # used for validating a message was sent
    activity: Optional[MessageActivity] = None  # sent with Rich Presence-related chat embeds
    application: Optional[MessageApplication] = None  # sent with Rich Presence-related chat embeds
    message_reference: Optional[MessageReference] = None  # reference data sent with crossposted messages
    guild_id: Optional[Snowflake] = None  # id of the guild the message was sent in
    member: Optional[GuildMember] = None  # member properties for this message's author

    pinned: bool = False  # whether this message is pinned
    type: int = -1  # type of message
    flags: Optional[int] = -1  #

