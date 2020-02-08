from dataclasses import dataclass

from ct.objects.role import Role
from ct.objects.user import User


@dataclass
class Presence:
    user: User
    roles: [Role]
    game: Activity