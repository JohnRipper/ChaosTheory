from dataclasses import dataclass


# attributes ending with _ are optionals.

class Snowflake:
    id: int


class Overwrite:
    id: int

class User:
    id: int

@dataclass
class Channel:
    id: Snowflake
    type: int
    guild_id_: Snowflake
    position_: int
    permission_overwrites_: [Overwrite]
    name_: str
    topic_: str
    nsfw_: bool
    last_message_id_: Snowflake
    bitrate_: int
    user_limit_: int
    rate_limit_per_user_: int
    recipients_: [User]
    icon_: str
    owner_id_: Snowflake
    application_id_: Snowflake
    parent_id_: Snowflake
    last_pin_timestamp_: str
