import importlib

from ct.objects.gateway import Ready
from ct.objects.message import Message


class CogManager:

    def igetattr(obj, attr):
        """case insensitive getattr for command router"""
        for a in dir(obj):
            if a.lower() == attr.lower():
                return getattr(obj, a)

    def __init__(self):
        self.cogs = {}
        self.imported = {}

    def import_module(self, name: str):
        # attempt to reload if already loaded
        if mod := self.imported.get(name, False):
            self.unload(name)
            if m := importlib.reload(mod):
                self.add_cog(mod=m, name=name, bot=bot)
        # not loaded? try loading.
        try:
            m = importlib.import_module(f"modules.{name}".lower())
            self.imported.update({name.lower(): m})

            return m
        except ModuleNotFoundError as e:
            print(e)

    def add_cog(self, name: str):
        if cls_obj := self.imported.get(name.lower(), False):
            cog = cls_obj()
            self.cogs.update({name: cog})
            return
        raise Exception("Could not find import")

    def unload_cog(self, name: str) -> bool:
        if name in self.cogs.keys():
            self.cogs.pop(name)
            return True
        return False

    def do_event(self, event, data):
            routes = {
                "READY": None,
                "GUILD_CREATE": None,
                "MESSAGE_CREATE": Message
            }
            test = routes.get(event, None)
            for cog in self.cogs:
                for e in cog.events:
                    if event == getattr(e, '__event__'):
                        e(test(**data))
            pass

    def do_command(self, command):
        pass