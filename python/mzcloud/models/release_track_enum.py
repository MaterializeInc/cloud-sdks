from enum import Enum


class ReleaseTrackEnum(str, Enum):
    CANARY = "canary"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
