from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.deployment_size_enum import DeploymentSizeEnum
from typing import Union
from ..types import UNSET, Unset
from typing import cast, List


T = TypeVar("T", bound="DeploymentRequest")


@attr.s(auto_attribs=True)
class DeploymentRequest:
    """  """

    name: Union[Unset, str] = UNSET
    size: Union[Unset, DeploymentSizeEnum] = DeploymentSizeEnum.XS
    storage_mb: Union[Unset, int] = 100
    disable_user_indexes: Union[Unset, bool] = False
    materialized_extra_args: Union[Unset, List[str]] = UNSET
    mz_version: Union[Unset, str] = UNSET
    enable_tailscale: Union[Unset, bool] = UNSET
    tailscale_auth_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        size: Union[Unset, str] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value

        storage_mb = self.storage_mb
        disable_user_indexes = self.disable_user_indexes
        materialized_extra_args: Union[Unset, List[str]] = UNSET
        if not isinstance(self.materialized_extra_args, Unset):
            materialized_extra_args = self.materialized_extra_args

        mz_version = self.mz_version
        enable_tailscale = self.enable_tailscale
        tailscale_auth_key = self.tailscale_auth_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if storage_mb is not UNSET:
            field_dict["storageMb"] = storage_mb
        if disable_user_indexes is not UNSET:
            field_dict["disableUserIndexes"] = disable_user_indexes
        if materialized_extra_args is not UNSET:
            field_dict["materializedExtraArgs"] = materialized_extra_args
        if mz_version is not UNSET:
            field_dict["mzVersion"] = mz_version
        if enable_tailscale is not UNSET:
            field_dict["enableTailscale"] = enable_tailscale
        if tailscale_auth_key is not UNSET:
            field_dict["tailscaleAuthKey"] = tailscale_auth_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _size = d.pop("size", UNSET)
        size: Union[Unset, DeploymentSizeEnum]
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = DeploymentSizeEnum(_size)

        storage_mb = d.pop("storageMb", UNSET)

        disable_user_indexes = d.pop("disableUserIndexes", UNSET)

        materialized_extra_args = cast(List[str], d.pop("materializedExtraArgs", UNSET))

        mz_version = d.pop("mzVersion", UNSET)

        enable_tailscale = d.pop("enableTailscale", UNSET)

        tailscale_auth_key = d.pop("tailscaleAuthKey", UNSET)

        deployment_request = cls(
            name=name,
            size=size,
            storage_mb=storage_mb,
            disable_user_indexes=disable_user_indexes,
            materialized_extra_args=materialized_extra_args,
            mz_version=mz_version,
            enable_tailscale=enable_tailscale,
            tailscale_auth_key=tailscale_auth_key,
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
