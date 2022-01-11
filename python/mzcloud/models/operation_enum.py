from enum import Enum


class OperationEnum(str, Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"

    def __str__(self) -> str:
        return str(self.value)
