# -*- coding: utf-8 -*-
#
# Copyright 2019, JohnnyCarcinogen ( https://github.com/JohnRipper/ ), All rights reserved.
#  
# logger.py Created by dev at 2/26/20
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

import os
import sys
from logging import Filter, LogRecord, addLevelName, getLoggerClass, setLoggerClass, StreamHandler, FileHandler, \
    Formatter
from datetime import date

project_path = os.path.dirname(os.path.realpath(__file__))

class ChaosLogger(getLoggerClass()):

    # Custom Levels
    CHAT = 70
    RECV = 20
    SENT = 30

    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 70
    WARN = 70
    ERROR = 80
    CRITICAL = 90

    _choices = ((CHAT, "chat"),
                (RECV, "recv"),
                (SENT, "sent"),
                (DEBUG, "debug"),
                (INFO, "info"),
                (WARNING, "warning"),
                (WARN, "warm"),
                (ERROR, "error"),
                (CRITICAL, "critical"),)

    log_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def __init__(self, name, level=20):
        super().__init__(name, level)
        addLevelName(self.CHAT, "CHAT")
        addLevelName(self.RECV, "RECV")
        addLevelName(self.SENT, "SENT")
        self.setLevel(level)

    def set_level(self, level):
        for choice in self._choices:
            if level == choice[0]:
                self._set_file_handler(level, choice[1])
                self.info(f"Logging level set to {choice[1]}")

        terminal_handler = StreamHandler(sys.stdout)
        terminal_handler.setLevel(level)
        terminal_handler.setFormatter(self.log_format)
        self.addHandler(terminal_handler)

    def chat(self, msg, *args, **kwargs):
        if self.isEnabledFor(self.CHAT):
            self._log(self.CHAT, msg, args, **kwargs)

    def recv(self, msg: str,  *args, **kwargs):
        if self.isEnabledFor(self.RECV):

            self._log(self.RECV, msg, args, **kwargs)

    def sent(self, msg, *args, **kwargs):
        if self.isEnabledFor(self.SENT):
            self._log(self.SENT, msg, args, **kwargs)

    def _set_file_handler(self, level, filename: str):
        filename = f"{filename}.log"
        # sort by time or limit log file size?
        # today = date.today().strftime("%b_%d_%y")
        log_path = f"logs/{filename}"
        # create path if it does not exist
        open(os.path.join(project_path, "..", "logs", filename), 'a').close()

        handler = FileHandler(filename=log_path)
        handler.setLevel(level)
        handler.setFormatter(self.log_format)
        self.addHandler(handler)


class ChatFilter(Filter):
    def filter(self, record: LogRecord):
        msg = record.msg
        if isinstance(msg, str):
            if record.levelno == ChaosLogger.CHAT:
                return True
            return False



setLoggerClass(ChaosLogger)
