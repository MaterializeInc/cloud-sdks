from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Optional
from ..types import UNSET, Unset
from typing import Union
from typing import cast
from typing import Dict
from ..models.deployment_size import DeploymentSize
from ..models.pending_migration import PendingMigration


T = TypeVar("T", bound="Deployment")


@attr.s(auto_attribs=True)
class Deployment:
    """  """

    id: str
    organization: str
    tls_authority: str
    name: str
    flagged_for_deletion: bool
    flagged_for_update: bool
    mz_version: str
    statefulset_status: str
    hostname: Optional[str]
    cluster_id: Optional[str]
    pending_migration: Optional[PendingMigration]
    size: Union[Unset, DeploymentSize] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        organization = self.organization
        tls_authority = self.tls_authority
        name = self.name
        flagged_for_deletion = self.flagged_for_deletion
        flagged_for_update = self.flagged_for_update
        mz_version = self.mz_version
        statefulset_status = self.statefulset_status
        hostname = self.hostname
        size: Union[Unset, str] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value

        cluster_id = self.cluster_id
        pending_migration = self.pending_migration.to_dict() if self.pending_migration else None

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
                "mzVersion": mz_version,
                "statefulsetStatus": statefulset_status,
                "hostname": hostname,
                "clusterId": cluster_id,
                "pendingMigration": pending_migration,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

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

        mz_version = d.pop("mzVersion")

        statefulset_status = d.pop("statefulsetStatus")

        hostname = d.pop("hostname")

        _size = d.pop("size", UNSET)
        size: Union[Unset, DeploymentSize]
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = DeploymentSize(_size)

        cluster_id = d.pop("clusterId")

        _pending_migration = d.pop("pendingMigration")
        pending_migration: Optional[PendingMigration]
        if _pending_migration is None:
            pending_migration = None
        else:
            pending_migration = PendingMigration.from_dict(_pending_migration)

        deployment = cls(
            id=id,
            organization=organization,
            tls_authority=tls_authority,
            name=name,
            flagged_for_deletion=flagged_for_deletion,
            flagged_for_update=flagged_for_update,
            mz_version=mz_version,
            statefulset_status=statefulset_status,
            hostname=hostname,
            size=size,
            cluster_id=cluster_id,
            pending_migration=pending_migration,
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
