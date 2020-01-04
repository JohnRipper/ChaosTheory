import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict

class OpCode(Enum):
    # todo document send/recieves.
    Dispatch = 0
    Heartbeat = 1
    Identify = 2
    StatusUpdate = 3
    VoiceStateUpdate = 4
    # used to resume a closed connection
    Resume = 6
    # used to tell clients to reconnect to the gateway
    Reconnect = 7
    RequestGuildMembers = 8
    InvalidSession = 9
    # sent immediately after connecting, contains heartbeat and server debug information
    Hello = 10
    # sent immediately following a client heartbeat that was received
    Heartbeat_ACK = 11

def default_field(object):
    return field(default_factory=lambda:object)

@dataclass
class Identity:
    token: str
    properties: Dict = default_field({
    "$os": "linux",
    "$browser": "ChaosTheory",
    "$device": "ChaosTheory"
  })

    def __discord__(self):
        return json.dumps({
            "op": 2,
            "d": self.__dict__,
            "s": 42,
            "t": "Identify"
        })

@dataclass
class GatewayDispatch:
    op: int
    # refer to quantum jump on dict conversion
    d: str

    # only for op code 0
    s: int = None
    t: str = None
