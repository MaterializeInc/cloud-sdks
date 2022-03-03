from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.modified_boolean import ModifiedBoolean
from ..models.modified_size import ModifiedSize
from ..models.modified_string import ModifiedString
from ..models.modified_string_list import ModifiedStringList
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoricalDeploymentChange")


@attr.s(auto_attribs=True)
class HistoricalDeploymentChange:
    """
    Attributes:
        name (Union[Unset, ModifiedString]):
        hostname (Union[Unset, ModifiedString]):
        flagged_for_deletion (Union[Unset, ModifiedBoolean]):
        flagged_for_update (Union[Unset, ModifiedBoolean]):
        catalog_restore_mode (Union[Unset, ModifiedBoolean]):
        size (Union[Unset, ModifiedSize]):
        disable_user_indexes (Union[Unset, ModifiedBoolean]):
        materialized_extra_args (Union[Unset, ModifiedStringList]):
        cluster_id (Union[Unset, ModifiedString]):
        mz_version (Union[Unset, ModifiedString]):
        enable_tailscale (Union[Unset, ModifiedBoolean]):
    """

    name: Union[Unset, ModifiedString] = UNSET
    hostname: Union[Unset, ModifiedString] = UNSET
    flagged_for_deletion: Union[Unset, ModifiedBoolean] = UNSET
    flagged_for_update: Union[Unset, ModifiedBoolean] = UNSET
    catalog_restore_mode: Union[Unset, ModifiedBoolean] = UNSET
    size: Union[Unset, ModifiedSize] = UNSET
    disable_user_indexes: Union[Unset, ModifiedBoolean] = UNSET
    materialized_extra_args: Union[Unset, ModifiedStringList] = UNSET
    cluster_id: Union[Unset, ModifiedString] = UNSET
    mz_version: Union[Unset, ModifiedString] = UNSET
    enable_tailscale: Union[Unset, ModifiedBoolean] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        hostname: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hostname, Unset):
            hostname = self.hostname.to_dict()

        flagged_for_deletion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flagged_for_deletion, Unset):
            flagged_for_deletion = self.flagged_for_deletion.to_dict()

        flagged_for_update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flagged_for_update, Unset):
            flagged_for_update = self.flagged_for_update.to_dict()

        catalog_restore_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.catalog_restore_mode, Unset):
            catalog_restore_mode = self.catalog_restore_mode.to_dict()

        size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()

        disable_user_indexes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disable_user_indexes, Unset):
            disable_user_indexes = self.disable_user_indexes.to_dict()

        materialized_extra_args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.materialized_extra_args, Unset):
            materialized_extra_args = self.materialized_extra_args.to_dict()

        cluster_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_id, Unset):
            cluster_id = self.cluster_id.to_dict()

        mz_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mz_version, Unset):
            mz_version = self.mz_version.to_dict()

        enable_tailscale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enable_tailscale, Unset):
            enable_tailscale = self.enable_tailscale.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if flagged_for_deletion is not UNSET:
            field_dict["flaggedForDeletion"] = flagged_for_deletion
        if flagged_for_update is not UNSET:
            field_dict["flaggedForUpdate"] = flagged_for_update
        if catalog_restore_mode is not UNSET:
            field_dict["catalogRestoreMode"] = catalog_restore_mode
        if size is not UNSET:
            field_dict["size"] = size
        if disable_user_indexes is not UNSET:
            field_dict["disableUserIndexes"] = disable_user_indexes
        if materialized_extra_args is not UNSET:
            field_dict["materializedExtraArgs"] = materialized_extra_args
        if cluster_id is not UNSET:
            field_dict["clusterId"] = cluster_id
        if mz_version is not UNSET:
            field_dict["mzVersion"] = mz_version
        if enable_tailscale is not UNSET:
            field_dict["enableTailscale"] = enable_tailscale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _name = d.pop("name", UNSET)
        name: Union[Unset, ModifiedString]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ModifiedString.from_dict(_name)

        _hostname = d.pop("hostname", UNSET)
        hostname: Union[Unset, ModifiedString]
        if isinstance(_hostname, Unset):
            hostname = UNSET
        else:
            hostname = ModifiedString.from_dict(_hostname)

        _flagged_for_deletion = d.pop("flaggedForDeletion", UNSET)
        flagged_for_deletion: Union[Unset, ModifiedBoolean]
        if isinstance(_flagged_for_deletion, Unset):
            flagged_for_deletion = UNSET
        else:
            flagged_for_deletion = ModifiedBoolean.from_dict(_flagged_for_deletion)

        _flagged_for_update = d.pop("flaggedForUpdate", UNSET)
        flagged_for_update: Union[Unset, ModifiedBoolean]
        if isinstance(_flagged_for_update, Unset):
            flagged_for_update = UNSET
        else:
            flagged_for_update = ModifiedBoolean.from_dict(_flagged_for_update)

        _catalog_restore_mode = d.pop("catalogRestoreMode", UNSET)
        catalog_restore_mode: Union[Unset, ModifiedBoolean]
        if isinstance(_catalog_restore_mode, Unset):
            catalog_restore_mode = UNSET
        else:
            catalog_restore_mode = ModifiedBoolean.from_dict(_catalog_restore_mode)

        _size = d.pop("size", UNSET)
        size: Union[Unset, ModifiedSize]
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = ModifiedSize.from_dict(_size)

        _disable_user_indexes = d.pop("disableUserIndexes", UNSET)
        disable_user_indexes: Union[Unset, ModifiedBoolean]
        if isinstance(_disable_user_indexes, Unset):
            disable_user_indexes = UNSET
        else:
            disable_user_indexes = ModifiedBoolean.from_dict(_disable_user_indexes)

        _materialized_extra_args = d.pop("materializedExtraArgs", UNSET)
        materialized_extra_args: Union[Unset, ModifiedStringList]
        if isinstance(_materialized_extra_args, Unset):
            materialized_extra_args = UNSET
        else:
            materialized_extra_args = ModifiedStringList.from_dict(_materialized_extra_args)

        _cluster_id = d.pop("clusterId", UNSET)
        cluster_id: Union[Unset, ModifiedString]
        if isinstance(_cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = ModifiedString.from_dict(_cluster_id)

        _mz_version = d.pop("mzVersion", UNSET)
        mz_version: Union[Unset, ModifiedString]
        if isinstance(_mz_version, Unset):
            mz_version = UNSET
        else:
            mz_version = ModifiedString.from_dict(_mz_version)

        _enable_tailscale = d.pop("enableTailscale", UNSET)
        enable_tailscale: Union[Unset, ModifiedBoolean]
        if isinstance(_enable_tailscale, Unset):
            enable_tailscale = UNSET
        else:
            enable_tailscale = ModifiedBoolean.from_dict(_enable_tailscale)

        historical_deployment_change = cls(
            name=name,
            hostname=hostname,
            flagged_for_deletion=flagged_for_deletion,
            flagged_for_update=flagged_for_update,
            catalog_restore_mode=catalog_restore_mode,
            size=size,
            disable_user_indexes=disable_user_indexes,
            materialized_extra_args=materialized_extra_args,
            cluster_id=cluster_id,
            mz_version=mz_version,
            enable_tailscale=enable_tailscale,
        )

        historical_deployment_change.additional_properties = d
        return historical_deployment_change

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
