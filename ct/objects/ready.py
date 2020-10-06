# -*- coding: utf-8 -*-
#
# Copyright 2019, JohnnyCarcinogen ( https://github.com/JohnRipper/ ), All rights reserved.
#  
# ready.py Created by dev at 4/7/20
# This file is part of ChaosTheory.
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from dataclasses import dataclass, field
from typing import List

from ct.objects.discord_object import DiscordObject
from ct.objects.user import User


@dataclass
class Ready(DiscordObject):
    v: int
    user_settings: None
    user: User
    application: None
    session_id: str
    _trace: List[str] = field(default_factory=list)
    relationships: List[User] = field(default_factory=User)
    private_channels: List[User] = field(default_factory=User)
    presences: List[User] = field(default_factory=User)
    guilds: List[User] = field(default_factory=User)
