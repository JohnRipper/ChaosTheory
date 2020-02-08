
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Audit_Log_Entry(DiscordObject):
   target_id: str = "" # id of the affected entity (webhook, user, role, etc.)
   changes_:   # changes made to the target_id
   user_id: Snowflake # the user who made the changes
   id: Snowflake # id of the entry
   action_type: Audit log event # type of action that occurred
   options_: Optional audit entry info # additional info for certain action types
   reason_: str = "" # the reason for the change (0-512 characters)

