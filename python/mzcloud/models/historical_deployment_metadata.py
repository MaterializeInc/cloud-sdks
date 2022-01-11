import datetime
from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.operation_enum import OperationEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoricalDeploymentMetadata")


@attr.s(auto_attribs=True)
class HistoricalDeploymentMetadata:
    """ """

    date: datetime.datetime
    user: str
    operation: OperationEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        user = self.user
        operation = self.operation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "user": user,
                "operation": operation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = isoparse(d.pop("date"))

        user = d.pop("user")

        operation = OperationEnum(d.pop("operation"))

        historical_deployment_metadata = cls(
            date=date,
            user=user,
            operation=operation,
        )

        historical_deployment_metadata.additional_properties = d
        return historical_deployment_metadata

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
