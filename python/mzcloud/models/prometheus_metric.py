from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrometheusMetric")


@attr.s(auto_attribs=True)
class PrometheusMetric:
    """ """

    name: str
    values: List[List[str]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        values = []
        for values_item_data in self.values:
            values_item = values_item_data

            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = cast(List[str], values_item_data)

            values.append(values_item)

        prometheus_metric = cls(
            name=name,
            values=values,
        )

        prometheus_metric.additional_properties = d
        return prometheus_metric

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
