from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

import attr

from ..models.provider_enum import ProviderEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportedCloudRegionRequest")


@attr.s(auto_attribs=True)
class SupportedCloudRegionRequest:
    """
    Attributes:
        provider (ProviderEnum):
        region (str):
    """

    provider: ProviderEnum
    region: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider.value

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = ProviderEnum(d.pop("provider"))

        region = d.pop("region")

        supported_cloud_region_request = cls(
            provider=provider,
            region=region,
        )

        supported_cloud_region_request.additional_properties = d
        return supported_cloud_region_request

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
