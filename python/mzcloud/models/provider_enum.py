from enum import Enum


class ProviderEnum(str, Enum):
    AWS = "AWS"

    def __str__(self) -> str:
        return str(self.value)
