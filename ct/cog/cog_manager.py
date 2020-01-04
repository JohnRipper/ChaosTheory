

class CogManager:

    def __init__(self):
        self.cogs = []
        self.imported = []

    def load(self, name: str):
        pass

    def reload(self, name: str):
        pass

    def unload(self, name: str):
        pass

    def do_event(self, event, data):
            routes = {
                "READY": None,
                "GUILD_CREATE": None
            }
            test = routes.get(event, None)
            for cog in self.cogs:
                for e in cog.events:
                    if event == getattr(e, '__event__'):
                        e(**test)
            pass

    def do_command(self, command):
        pass