# -*- coding: utf-8 -*-
#
# Copyright 2019, JohnnyCarcinogen ( https://github.com/JohnRipper/ ), All rights reserved.
#  
# command.py Created by dev at 3/27/20
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
import re

from ct.objects.message import Message


def makeCommand(aliases: [], description: str):
    def wrap(f):
        f.__command__ = True
        f.command_aliases = aliases
        f.__description__ = description
        return f

    return wrap


class Command:
    CMD_PATTERN = command_pattern = "{}(\w+)(\\b.*)"

    def __init__(self, prefix: str, data: dict):
        self.prefix = prefix
        self.message = Message(**data)
        self.name = "not found"
        parsed = re.search(self.CMD_PATTERN.format(prefix), self.message.content)
        self.raw_message = self.message.content
        if parsed is not None:
            self.name, self.message.content = parsed.groups()
