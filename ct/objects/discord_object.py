import re as regex
from dataclasses import dataclass, fields, is_dataclass


# parent object


@dataclass()
class DiscordObject:

    def __post_init__(instance):
        """Convert all fields of type `dataclass` into an instance of the
        specified data class if the current value is of type dict."""
        cls = type(instance)
        for f in fields(cls):
            if not is_dataclass(f.type):
                continue

            value = getattr(instance, f.name)
            if not isinstance(value, dict):
                continue

            new_value = f.type(**value)
            setattr(instance, f.name, new_value)

    def del_none(self, d):
        """
        Delete keys with the value ``None`` in a dictionary, recursively.

        This alters the input so you may wish to ``copy`` the dict first.
        """
        # For Python 3, write `list(d.items())`; `d.items()` won’t work
        for key, value in list(d.items()):
            if value is None:
                del d[key]
            elif isinstance(value, dict):
                self.del_none(value)
        return d  # For convenience

    def get_required_fields(self) -> list:
        return [field.name for field in fields(self) if not self.__is_optional_field(field)]

    def get_optional_fields(self) -> list:
        return [field.name for field in fields(self) if self.__is_optional_field(field)]

    def __is_optional_field(self, field) -> bool:
        pattern = '\Atyping.Union\[.*, NoneType\]\Z'
        return regex.match(pattern, str(field.type)) is not None
