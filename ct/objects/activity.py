from dataclasses import dataclass
from enum import Enum

from ct.objects.guild import Guild
from ct.objects.snowflake import Snowflake
from ct.objects.user import User

class ActivityType(Enum):
    NoType = -1  # just something i added incase of error.
    Game = 0  # Format: "Playing {name}"
    Streaming = 1  # Format: "Playing {name}"
    Listening = 2  # Format: "Playing {name}"
    Custom = 4  # Format: "Playing {name}"


@dataclass
class ActivityTimeStamps:
    start: int = -1  # unix time (in milliseconds) of when the activity started
    end: int = -1  # unix time (in milliseconds) of when the activity ended


@dataclass
class ActivityEmoji:
    id: Snowflake  # id of the emoji
    name: str = ""  # name of the emoji
    animated: bool = False  # whether the emoji is animated


@dataclass
class ActivityAssets:
    large_image: str = ""  # the id of the large asset of the activity, usually a snowflake
    small_image: str = ""  # the id of the small asset of the activity, usually a snowflake
    large_text: str = ""  # text displayed when hovering over the large image of the activity
    small_text: str = ""  # text displayed when hovering over the small image of the activity


@dataclass
class ActivitySecrets:
    join: str = ""  # the secret for joining a party
    spectate: str = ""  # the secret for spectating a game
    match: str = ""  # the secret for a specific instanced match

ch
@dataclass
class ActivityParty:
    id: str = ""  # the id of the party
    size: int = -1  # the parties current and maximum size


@dataclass
class Activity:
    timestamps: ActivityTimeStamps
    name: str = ""  # The activities name
    type: ActivityType = ActivityType.NoType  # activity Type
    url_: str = "" # stream url is validated when type is 1
    created_at: int = -1
