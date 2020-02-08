
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Invite(DiscordObject):
   code: str = "" # the invite code (unique ID)
   guild_:   # the guild this invite is for
   channel:   # the channel this invite is for
   inviter_:   # the user who created the invite
   target_user_:   # the target user for this invite
   target_user_type_: int = -1 # the type of target user for this invite
   approximate_presence_count_: int = -1 # approximate count of online members (only present when target_user is set)
   approximate_member_count_: int = -1 # approximate count of total members

