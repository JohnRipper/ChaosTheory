from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from ct.objects.discord_object import DiscordObject


class ActivityType(Enum):
    NoType = -1  # just something i added incase of error.
    Game = 0  # Format: "Playing {name}"
    Streaming = 1  # Format: "Playing {name}"
    Listening = 2  # Format: "Playing {name}"
    Custom = 4  # Format: "Playing {name}"


@dataclass
class ActivityTimeStamps(DiscordObject):
    start: int = -1  # unix time (in milliseconds) of when the activity started
    end: int = -1  # unix time (in milliseconds) of when the activity ended


@dataclass
class ActivityEmoji(DiscordObject):
    name: str = ""  # name of the emoji
    animated: Optional[bool] = field(default=None)  # whether the emoji is animated
    id: Optional[int] = field(default=None)  # id of the emoji


@dataclass
class ActivityAssets(DiscordObject):
    large_image: str = ""  # the id of the large asset of the activity, usually a snowflake
    small_image: str = ""  # the id of the small asset of the activity, usually a snowflake
    large_text: str = ""  # text displayed when hovering over the large image of the activity
    small_text: str = ""  # text displayed when hovering over the small image of the activity


@dataclass
class ActivitySecrets(DiscordObject):
    join: str = ""  # the secret for joining a party
    spectate: str = ""  # the secret for spectating a game
    match: str = ""  # the secret for a specific instanced match


@dataclass
class ActivityParty(DiscordObject):
    id: Optional[str] = field(default=None)  # the id of the party
    size: Optional[tuple] = field(default=None)  # the parties current and maximum size


@dataclass
class Activity(DiscordObject):
    created_at: int
    name: str  # The activities name

    id: Optional[int] = field(default=None)  # id of the message

    application_id: Optional[int] = field(default=None)
    type: ActivityType = ActivityType.NoType  # activity Type
    timestamps: Optional[ActivityTimeStamps] = field(default=None)  #
    url: Optional[str] = field(default=None)  # stream url is validated when type is 1
    details: Optional[str] = field(default=None)
    state: Optional[str] = field(default=None)
    session_id: Optional[str] = field(default=None)  # the user presence is being updated for
    sync_id: Optional[str] = field(default=None)
    platform: Optional[str] = field(default=None)
    emoji: Optional[ActivityEmoji] = field(default=None)
    party: Optional[ActivityParty] = field(default=None)
    assets: Optional[ActivityAssets] = field(default=None)
    secrets: Optional[ActivitySecrets] = field(default=None)
    instance: Optional[bool] = field(default=None)
    flags: Optional[int] = field(default=None)
