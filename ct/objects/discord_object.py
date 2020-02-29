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

    def __dict__(self):
        dict = {}
        for field in fields(self):
            if self.__is_optional_field(field):
                print(f"ftype {field.type}")
                if str(field.type) != "Nonetype":
                    dict.update({str(field.name): getattr(self, str(field.name))})
        print(dict)
        return dict


    def get_required_fields(self) -> list:
        return [field.name for field in fields(self) if not self.__is_optional_field(field)]

    def get_optional_fields(self) -> list:
        return [field.name for field in fields(self) if self.__is_optional_field(field)]

    def __is_optional_field(self, field) -> bool:
        pattern = '\Atyping.Union\[.*, NoneType\]\Z'
        return regex.match(pattern, str(field.type)) is not None

