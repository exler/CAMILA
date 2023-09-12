import json
from pathlib import Path
from typing import Self, Type


class Settings:
    OPENAI_API_KEY: str

    STORE_PERSIST_DIRECTORY_PATH: Path = Path(__file__).parent.parent

    @classmethod
    def from_json(cls: Type[Self], path: Path | str) -> Self:
        with Path.open(path, "r") as f:
            data = json.load(f)

        instance = cls()

        for key, value in data.items():
            # Get type hinting from the class
            type_hint = cls.__annotations__.get(key)
            # If type hint found, convert the value to the type hint
            if type_hint:
                value = type_hint(value)
            # Set the attribute on the instance
            setattr(instance, key, value)

        return instance
