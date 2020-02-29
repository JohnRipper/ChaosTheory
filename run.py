import asyncio
import sys

from ct.client import Client
from ct.config import Configuration

# read configuration file.
try:
    config = Configuration("./config/default.toml")
except FileNotFoundError:
    # todo a file generator? think of a better way than quantum 1,2
    sys.exit()


# load client
c = Client(token='')

# connect
asyncio.get_event_loop().run_until_complete(c.connect())
