from dataclasses import dataclass

from ct.objects.guild import Guild
from ct.objects.user import User

@dataclass
class Ready:
    v: int
    user: User
    private_channels: []
    guilds: [Guild]
    session_id: str
    shard: []