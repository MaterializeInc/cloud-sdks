from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from ..models.pending_migration import PendingMigration
from typing import cast
from ..types import UNSET, Unset
from typing import Union
from ..models.deployment_size import DeploymentSize
from typing import Optional




T = TypeVar("T", bound="Deployment")

@attr.s(auto_attribs=True)
class Deployment:
    """  """
    id: str
    organization: str
    tls_authority: str
    name: str
    hostname: str
    flagged_for_deletion: bool
    flagged_for_update: bool
    cluster_id: str
    mz_version: str
    statefulset_status: str
    pending_migration: Optional[PendingMigration]
    size: Union[Unset, DeploymentSize] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        organization = self.organization
        tls_authority = self.tls_authority
        name = self.name
        hostname = self.hostname
        flagged_for_deletion = self.flagged_for_deletion
        flagged_for_update = self.flagged_for_update
        cluster_id = self.cluster_id
        mz_version = self.mz_version
        statefulset_status = self.statefulset_status
        size: Union[Unset, str] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value

        pending_migration = self.pending_migration.to_dict() if self.pending_migration else None


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "organization": organization,
            "tlsAuthority": tls_authority,
            "name": name,
            "hostname": hostname,
            "flaggedForDeletion": flagged_for_deletion,
            "flaggedForUpdate": flagged_for_update,
            "clusterId": cluster_id,
            "mzVersion": mz_version,
            "statefulsetStatus": statefulset_status,
            "pendingMigration": pending_migration,
        })
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

        hostname = d.pop("hostname")

        flagged_for_deletion = d.pop("flaggedForDeletion")

        flagged_for_update = d.pop("flaggedForUpdate")

        cluster_id = d.pop("clusterId")

        mz_version = d.pop("mzVersion")

        statefulset_status = d.pop("statefulsetStatus")

        _size = d.pop("size", UNSET)
        size: Union[Unset, DeploymentSize]
        if isinstance(_size,  Unset):
            size = UNSET
        else:
            size = DeploymentSize(_size)




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
            hostname=hostname,
            flagged_for_deletion=flagged_for_deletion,
            flagged_for_update=flagged_for_update,
            cluster_id=cluster_id,
            mz_version=mz_version,
            statefulset_status=statefulset_status,
            size=size,
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
