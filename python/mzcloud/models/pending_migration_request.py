from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from dateutil.parser import isoparse
import datetime




T = TypeVar("T", bound="PendingMigrationRequest")

@attr.s(auto_attribs=True)
class PendingMigrationRequest:
    """  """
    description: str
    deadline: datetime.date
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        deadline = self.deadline.isoformat() 

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "description": description,
            "deadline": deadline,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        deadline = isoparse(d.pop("deadline")).date()




        pending_migration_request = cls(
            description=description,
            deadline=deadline,
        )

        pending_migration_request.additional_properties = d
        return pending_migration_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
