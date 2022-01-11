from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.deployment_size_enum import DeploymentSizeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedDeploymentUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedDeploymentUpdateRequest:
    """ """

    name: Union[Unset, str] = UNSET
    catalog_restore_mode: Union[Unset, bool] = False
    size: Union[Unset, DeploymentSizeEnum] = DeploymentSizeEnum.XS
    storage_mb: Union[Unset, int] = 100
    disable_user_indexes: Union[Unset, bool] = False
    materialized_extra_args: Union[Unset, List[str]] = UNSET
    mz_version: Union[Unset, str] = UNSET
    enable_tailscale: Union[Unset, bool] = False
    tailscale_auth_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        catalog_restore_mode = self.catalog_restore_mode
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
        if catalog_restore_mode is not UNSET:
            field_dict["catalogRestoreMode"] = catalog_restore_mode
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

        catalog_restore_mode = d.pop("catalogRestoreMode", UNSET)

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

        patched_deployment_update_request = cls(
            name=name,
            catalog_restore_mode=catalog_restore_mode,
            size=size,
            storage_mb=storage_mb,
            disable_user_indexes=disable_user_indexes,
            materialized_extra_args=materialized_extra_args,
            mz_version=mz_version,
            enable_tailscale=enable_tailscale,
            tailscale_auth_key=tailscale_auth_key,
        )

        patched_deployment_update_request.additional_properties = d
        return patched_deployment_update_request

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
