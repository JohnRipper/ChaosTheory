from dataclasses import dataclass, fields
import re as regex


# parent object
@dataclass()
class DiscordObject:

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

