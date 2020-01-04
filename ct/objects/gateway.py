from dataclasses import dataclass
from ct.objects.user import User

@dataclass
class Ready:
    v: int
    user: User
    private_channels: []
    guids: [UnavailableGuild]
    session_id: str
    shard: []