from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.create_phone_number_response_200_linked_to_item_type import CreatePhoneNumberResponse200LinkedToItemType

T = TypeVar("T", bound="CreatePhoneNumberResponse200LinkedToItem")


@_attrs_define
class CreatePhoneNumberResponse200LinkedToItem:
    """
    Attributes:
        type (CreatePhoneNumberResponse200LinkedToItemType):
        id (str):
    """

    type: CreatePhoneNumberResponse200LinkedToItemType
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
        type = CreatePhoneNumberResponse200LinkedToItemType(d.pop("type"))

        id = d.pop("id")

        create_phone_number_response_200_linked_to_item = cls(
            type=type,
            id=id,
        )

        return create_phone_number_response_200_linked_to_item