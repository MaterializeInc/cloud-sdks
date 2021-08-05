from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from ..models.deployment_size import DeploymentSize


T = TypeVar("T", bound="PatchedDeploymentRequest")


@attr.s(auto_attribs=True)
class PatchedDeploymentRequest:
    """  """

    size: Union[Unset, DeploymentSize] = UNSET
    mz_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size: Union[Unset, str] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value

        mz_version = self.mz_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if mz_version is not UNSET:
            field_dict["mzVersion"] = mz_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _size = d.pop("size", UNSET)
        size: Union[Unset, DeploymentSize]
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = DeploymentSize(_size)

        mz_version = d.pop("mzVersion", UNSET)

        patched_deployment_request = cls(
            size=size,
            mz_version=mz_version,
        )

        patched_deployment_request.additional_properties = d
        return patched_deployment_request

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
