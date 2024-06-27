from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2ErrorType1Type0Meta")


@_attrs_define
class SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2ErrorType1Type0Meta:
    """ """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_2_error_type_1_type_0_meta = (
            cls()
        )

        set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_2_error_type_1_type_0_meta.additional_properties = d
        return (
            set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_2_error_type_1_type_0_meta
        )

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
