import asyncio
import websockets
from ct.client import Client
from ct.config import Configuration
import sys

# read configuration file.
try:
    config = Configuration("./config/default.toml")
except FileNotFoundError:
    # todo a file generator? think of a better way than quantum 1,2
    sys.exit()


# load client
c = Client(token='NjYzMDgwNzY4NzYzMDY4NDIw.XhD98A.0r5rJR7KotlSQzDAzfK1qkP9Sw8')

# connect
asyncio.get_event_loop().run_until_complete(c.connect())