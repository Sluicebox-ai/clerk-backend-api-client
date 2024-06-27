from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_organizations_response_200_data_item import ListOrganizationsResponse200DataItem


T = TypeVar("T", bound="ListOrganizationsResponse200")


@_attrs_define
class ListOrganizationsResponse200:
    """
    Attributes:
        data (List['ListOrganizationsResponse200DataItem']):
        total_count (int): Total number of organizations
    """

    data: List["ListOrganizationsResponse200DataItem"]
    total_count: int

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "data": data,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_organizations_response_200_data_item import ListOrganizationsResponse200DataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListOrganizationsResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        total_count = d.pop("total_count")

        list_organizations_response_200 = cls(
            data=data,
            total_count=total_count,
        )

        return list_organizations_response_200
