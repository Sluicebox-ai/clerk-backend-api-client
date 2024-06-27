from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.lock_user_response_200_email_addresses_item_linked_to_item_type import (
    LockUserResponse200EmailAddressesItemLinkedToItemType,
)

T = TypeVar("T", bound="LockUserResponse200EmailAddressesItemLinkedToItem")


@_attrs_define
class LockUserResponse200EmailAddressesItemLinkedToItem:
    """
    Attributes:
        type (LockUserResponse200EmailAddressesItemLinkedToItemType):
        id (str):
    """

    type: LockUserResponse200EmailAddressesItemLinkedToItemType
    id: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = LockUserResponse200EmailAddressesItemLinkedToItemType(d.pop("type"))

        id = d.pop("id")

        lock_user_response_200_email_addresses_item_linked_to_item = cls(
            type=type,
            id=id,
        )

        return lock_user_response_200_email_addresses_item_linked_to_item
