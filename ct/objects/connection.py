
from dataclasses import dataclass
from ct.objects.discordobject import DiscordObject

@dataclass
class Connection(DiscordObject):
   id: str = "" # id of the connection account
   name: str = "" # the username of the connection account
   type: str = "" # the service of the connection (twitch, youtube)
   revoked: bool = False # whether the connection is revoked
   integrations: Array #  
   verified: bool = False # whether the connection is verified
   friend_sync: bool = False # whether friend sync is enabled for this connection
   show_activity: bool = False # whether activities related to this connection will be shown in presence updates
   visibility: int = -1 #  

