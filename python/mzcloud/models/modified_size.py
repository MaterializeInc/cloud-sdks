from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

import attr

from ..models.deployment_size_enum import DeploymentSizeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifiedSize")


@attr.s(auto_attribs=True)
class ModifiedSize:
    """ """

    old: DeploymentSizeEnum
    new: DeploymentSizeEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        old = self.old.value

        new = self.new.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old": old,
                "new": new,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        old = DeploymentSizeEnum(d.pop("old"))

        new = DeploymentSizeEnum(d.pop("new"))

        modified_size = cls(
            old=old,
            new=new,
        )

        modified_size.additional_properties = d
        return modified_size

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
