import asyncio
import importlib
from types import ModuleType

from ct.command import Command
from ct.objects.gateway import Ready
from ct.objects.message import Message
from ct.objects.presence import Presence
from ct.objects.voice_server_update import VoiceServerUpdate
from ct.objects.voice_state import VoiceState


class CogManager:

    def igetattr(self, obj, attr):
        """case insensitive getattr for command router"""
        for a in dir(obj):
            if a.lower() == attr.lower():
                return getattr(obj, a)

    def __init__(self):
        self.cogs = {}
        self.imported = {}

    def import_module(self, module: str, bot) -> ModuleType:
        # attempt to reload if already loaded
        if mod := self.imported.get(module, False):
            self.unload_cog(module)
            if m := importlib.reload(mod):
                self.add_cog(module=m, name=module, bot=bot)
        # not loaded? try loading.
        try:
            m = importlib.import_module(f"modules.{module}".lower())
            self.imported.update({module: m})
            self.add_cog(module=m, name=module, bot=bot)

            return m
        except ModuleNotFoundError as e:
            print(e)

    def add_cog(self, module: ModuleType,  name: str, bot):
        cog = self.igetattr(module, name)
        self.cogs.update({name: cog(bot)})

    def unload_cog(self, name: str) -> bool:
        if name in self.cogs.keys():
            self.cogs.pop(name)
            return True
        return False



    async def do_event(self, event: str, data: dict):
            routes = {
                "READY": Ready,
                "GUILD_CREATE": None,
                "MESSAGE_CREATE": Message,
                "VOICE_SERVER_UPDATE": VoiceServerUpdate,
                "VOICE_STATE_UPDATE": VoiceState,
                "PRESENCE_UPDATE": Presence
            }
            print(f"Attempting {event}")
            if choice := routes.get(event, False):
                for cog in self.cogs.values():
                    for meth in cog.events:
                        if meth.__event__ == event:
                            asyncio.create_task(meth(choice(**data)))

    async def do_command(self, command: Command):
        print(f"Attempting {command.name}")
        for cog in self.cogs.values():
            for meth in cog.commands:
                if command.name in meth.command_aliases:
                    asyncio.create_task(meth(command))
