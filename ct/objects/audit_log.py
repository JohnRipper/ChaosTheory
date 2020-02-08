
from dataclasses import dataclass
from ct.objects.discord_object import DiscordObject

from ct.objects.audit_log_entry import Audit_Log_Entry
from ct.objects.integration import Integration
from ct.objects.user import User
from ct.objects.webhook import Webhook


@dataclass
class Audit_Log(DiscordObject):
   webhooks: [Webhook]  # list of webhooks found in the audit log
   users: [User]  # list of users found in the audit log
   audit_log_entries: [Audit_Log_Entry]  # list of audit log entries
   integrations: [Integration]  # list of partial integration objects

