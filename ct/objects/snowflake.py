from dataclasses import dataclass


@dataclass
class Snowflake:
    id: str = ""
    # needs custom init
    def __init__(self):
        pass
