import datetime
from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """
    Attributes:
        id (str):
        deployment_limit (int):
        trial_expires_at (Optional[datetime.datetime]): When this organization's trial period expires. If empty, the
            organization is on an enterprise plan.
    """

    id: str
    deployment_limit: int
    trial_expires_at: Optional[datetime.datetime]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        deployment_limit = self.deployment_limit
        trial_expires_at = self.trial_expires_at.isoformat() if self.trial_expires_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deploymentLimit": deployment_limit,
                "trialExpiresAt": trial_expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        deployment_limit = d.pop("deploymentLimit")

        _trial_expires_at = d.pop("trialExpiresAt")
        trial_expires_at: Optional[datetime.datetime]
        if _trial_expires_at is None:
            trial_expires_at = None
        else:
            trial_expires_at = isoparse(_trial_expires_at)

        organization = cls(
            id=id,
            deployment_limit=deployment_limit,
            trial_expires_at=trial_expires_at,
        )

        organization.additional_properties = d
        return organization

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
