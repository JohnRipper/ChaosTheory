# -*- coding: utf-8 -*-
#
# Copyright 2019, JohnnyCarcinogen ( https://github.com/JohnRipper/ ), All rights reserved.
#  
# client_status.py Created by JohnnyCarcinogen at 2/10/20
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
from typing import Optional

from ct.objects.discord_object import DiscordObject


@dataclass
class ClientStatus(DiscordObject):
	desktop: Optional[str] = field(default=None)
	mobile: Optional[str] = field(default=None)
	web: Optional[str] = field(default=None)

	def online(self):
		message = ''
		if self.desktop is not None:
			message = 'desktop'
		elif self.mobile is not None:
			message = 'mobile'
		elif self.web is not None:
			message = 'web'
		else:
			message = 'None'
