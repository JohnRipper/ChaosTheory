from dataclasses import make_dataclass
from pathlib import Path

from tomlkit import dumps as tomldump
from tomlkit import loads as tomlload
from tomlkit import items as tomltypes

from ct.util import prompt


class Configuration:
    def __init__(self, path: str):
        self.path = Path(path)
        if self.path.exists():
            self.full = self.load()
            self.bot = make_dataclass("Bot_Configuration",
                                      [(k, type(v), v)
                                       for k, v in self.full["Bot"].items()])
            self.Modules = self.full["Modules"]
        else:
            raise FileNotFoundError(path)

    def load(self) -> dict:
        config = tomlload(self.path.read_text())
        return config


def getmodules() -> list:
    modules = []
    # todo, module folders?
    module_files = Path("modules/").glob("*.py")
    for mod in module_files:
        if mod.name.startswith("__") is False:
            module = mod.name.rstrip(".py").capitalize()
            modules.append(module)
    return modules


def generate_config():
    config = tomlload(Path("example.toml").read_text())
    botsettings = config["Bot"]
    for each in botsettings.keys():
        if type(botsettings[each]) == bool:
            botsettings[each] = prompt(f"Would you like to enable {each}? y/N ")
        elif type(botsettings[each]) == tomltypes.Integer:
            numerical_option = input(f"Please enter a number for {each}: ")
            assert numerical_option.isdigit() is True, "Must be a number!"
            botsettings[each] = int(numerical_option)
        else:
            botsettings[each] = input(f"Please enter your {each}: ")
    modules = getmodules()
    print(
        "Enter the number for each module you'd like to enable, separated by commas"
    )
    print("Example: 1,5,8")
    message = ", ".join([f"{i}) {v}" for i, v in enumerate(modules)])
    to_enable = input(f"{message}\n")
    for module_index in to_enable.split(","):
        if module_index.isdigit() and int(module_index) <= len(modules):
            config["Modules"]["enabled"].append(modules[int(module_index)])
    return tomldump(config)


def write_config(config: str, path: str) -> bool:
    check = prompt(f"\n{config}\nDoes this look correct? y/N")
    if check is False:
        return False
    else:
        path = Path.joinpath(Path.cwd(), path)
        with open(path, "w") as toml:
            toml.write(config)
        return True