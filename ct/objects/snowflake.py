from dataclasses import dataclass


@dataclass
class Snowflake:
    id: str = ""

    # needs custom init
    def __init__(self, **kwargs):
        self.id = 0
        pass
