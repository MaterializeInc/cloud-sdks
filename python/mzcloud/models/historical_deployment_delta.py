from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

import attr

from ..models.historical_deployment_change import HistoricalDeploymentChange
from ..models.historical_deployment_metadata import HistoricalDeploymentMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoricalDeploymentDelta")


@attr.s(auto_attribs=True)
class HistoricalDeploymentDelta:
    """ """

    changes: HistoricalDeploymentChange
    metadata: HistoricalDeploymentMetadata
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        changes = self.changes.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changes": changes,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        changes = HistoricalDeploymentChange.from_dict(d.pop("changes"))

        metadata = HistoricalDeploymentMetadata.from_dict(d.pop("metadata"))

        historical_deployment_delta = cls(
            changes=changes,
            metadata=metadata,
        )

        historical_deployment_delta.additional_properties = d
        return historical_deployment_delta

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
