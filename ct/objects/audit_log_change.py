
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

class AuditLogChangeKey(DiscordObject):
    name: str
    object_changed: str
    type: str

@dataclass
class AuditLogChange(DiscordObject):
   new_value_: Mixed  # new value of the key
   old_value_: Mixed  # old value of the key
   key: str = ""  # name of audit log change key

