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
c = Client(token='Mzg4MTQ3MjE0NDQ4NDU5Nzc5.XiRv1A._HA3M_Cng8L2_RaeB65Lz-ImuPQ')

# connect
asyncio.get_event_loop().run_until_complete(c.connect())
