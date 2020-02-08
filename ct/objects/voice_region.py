
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Voice_Region(DiscordObject):
   id: str = "" # unique ID for the region
   name: str = "" # name of the region
   vip: bool = False # true if this is a vip-only server
   optimal: bool = False # true for a single server that is closest to the current user's client
   deprecated: bool = False # whether this is a deprecated voice region (avoid switching to these)
   custom: bool = False # whether this is a custom voice region (used for events/etc)

