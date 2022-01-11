from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

import attr

from ..models.deployment_size_enum import DeploymentSizeEnum
from ..models.supported_cloud_region import SupportedCloudRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="Deployment")


@attr.s(auto_attribs=True)
class Deployment:
    """ """

    id: str
    organization: str
    tls_authority: str
    name: str
    flagged_for_deletion: bool
    flagged_for_update: bool
    materialized_extra_args: List[str]
    mz_version: str
    status: str
    cloud_provider_region: SupportedCloudRegion
    hostname: Optional[str]
    cluster_id: Optional[str]
    catalog_restore_mode: bool = False
    size: DeploymentSizeEnum = DeploymentSizeEnum.XS
    storage_mb: int = 100
    disable_user_indexes: bool = False
    enable_tailscale: bool = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        organization = self.organization
        tls_authority = self.tls_authority
        name = self.name
        flagged_for_deletion = self.flagged_for_deletion
        flagged_for_update = self.flagged_for_update
        catalog_restore_mode = self.catalog_restore_mode
        size = self.size.value

        storage_mb = self.storage_mb
        disable_user_indexes = self.disable_user_indexes
        materialized_extra_args = self.materialized_extra_args

        mz_version = self.mz_version
        status = self.status
        enable_tailscale = self.enable_tailscale
        cloud_provider_region = self.cloud_provider_region.to_dict()

        hostname = self.hostname
        cluster_id = self.cluster_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization": organization,
                "tlsAuthority": tls_authority,
                "name": name,
                "flaggedForDeletion": flagged_for_deletion,
                "flaggedForUpdate": flagged_for_update,
                "catalogRestoreMode": catalog_restore_mode,
                "size": size,
                "storageMb": storage_mb,
                "disableUserIndexes": disable_user_indexes,
                "materializedExtraArgs": materialized_extra_args,
                "mzVersion": mz_version,
                "status": status,
                "enableTailscale": enable_tailscale,
                "cloudProviderRegion": cloud_provider_region,
                "hostname": hostname,
                "clusterId": cluster_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        organization = d.pop("organization")

        tls_authority = d.pop("tlsAuthority")

        name = d.pop("name")

        flagged_for_deletion = d.pop("flaggedForDeletion")

        flagged_for_update = d.pop("flaggedForUpdate")

        catalog_restore_mode = d.pop("catalogRestoreMode")

        size = DeploymentSizeEnum(d.pop("size"))

        storage_mb = d.pop("storageMb")

        disable_user_indexes = d.pop("disableUserIndexes")

        materialized_extra_args = cast(List[str], d.pop("materializedExtraArgs"))

        mz_version = d.pop("mzVersion")

        status = d.pop("status")

        enable_tailscale = d.pop("enableTailscale")

        cloud_provider_region = SupportedCloudRegion.from_dict(d.pop("cloudProviderRegion"))

        hostname = d.pop("hostname")

        cluster_id = d.pop("clusterId")

        deployment = cls(
            id=id,
            organization=organization,
            tls_authority=tls_authority,
            name=name,
            flagged_for_deletion=flagged_for_deletion,
            flagged_for_update=flagged_for_update,
            catalog_restore_mode=catalog_restore_mode,
            size=size,
            storage_mb=storage_mb,
            disable_user_indexes=disable_user_indexes,
            materialized_extra_args=materialized_extra_args,
            mz_version=mz_version,
            status=status,
            enable_tailscale=enable_tailscale,
            cloud_provider_region=cloud_provider_region,
            hostname=hostname,
            cluster_id=cluster_id,
        )

        deployment.additional_properties = d
        return deployment

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
