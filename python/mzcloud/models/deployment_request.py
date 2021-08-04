from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from ..models.deployment_request_size import DeploymentRequestSize




T = TypeVar("T", bound="DeploymentRequest")

@attr.s(auto_attribs=True)
class DeploymentRequest:
    """  """
    mz_version: str
    size: Union[Unset, DeploymentRequestSize] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        mz_version = self.mz_version
        size: Union[Unset, str] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mzVersion": mz_version,
        })
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mz_version = d.pop("mzVersion")

        _size = d.pop("size", UNSET)
        size: Union[Unset, DeploymentRequestSize]
        if isinstance(_size,  Unset):
            size = UNSET
        else:
            size = DeploymentRequestSize(_size)




        deployment_request = cls(
            mz_version=mz_version,
            size=size,
        )

        deployment_request.additional_properties = d
        return deployment_request

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
