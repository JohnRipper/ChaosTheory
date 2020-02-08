
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Audit_Log_Change(DiscordObject):
   new_value_: Mixed # new value of the key
   old_value_: Mixed # old value of the key
   key: str = "" #  

