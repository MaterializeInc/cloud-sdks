from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifiedStringList")


@attr.s(auto_attribs=True)
class ModifiedStringList:
    """
    Attributes:
        old (List[Optional[str]]):
        new (List[Optional[str]]):
    """

    old: List[Optional[str]]
    new: List[Optional[str]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        old = self.old

        new = self.new

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
        old = cast(List[Optional[str]], d.pop("old"))

        new = cast(List[Optional[str]], d.pop("new"))

        modified_string_list = cls(
            old=old,
            new=new,
        )

        modified_string_list.additional_properties = d
        return modified_string_list

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
