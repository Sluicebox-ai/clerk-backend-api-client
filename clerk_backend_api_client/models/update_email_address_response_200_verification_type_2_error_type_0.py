from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_email_address_response_200_verification_type_2_error_type_0_meta import (
        UpdateEmailAddressResponse200VerificationType2ErrorType0Meta,
    )


T = TypeVar("T", bound="UpdateEmailAddressResponse200VerificationType2ErrorType0")


@_attrs_define
class UpdateEmailAddressResponse200VerificationType2ErrorType0:
    """
    Attributes:
        message (str):
        long_message (str):
        code (str):
        meta (Union[Unset, UpdateEmailAddressResponse200VerificationType2ErrorType0Meta]):
        clerk_trace_id (Union[Unset, str]):
    """

    message: str
    long_message: str
    code: str
    meta: Union[Unset, "UpdateEmailAddressResponse200VerificationType2ErrorType0Meta"] = UNSET
    clerk_trace_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        long_message = self.long_message

        code = self.code

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        clerk_trace_id = self.clerk_trace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "long_message": long_message,
                "code": code,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if clerk_trace_id is not UNSET:
            field_dict["clerk_trace_id"] = clerk_trace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_email_address_response_200_verification_type_2_error_type_0_meta import (
            UpdateEmailAddressResponse200VerificationType2ErrorType0Meta,
        )

        d = src_dict.copy()
        message = d.pop("message")

        long_message = d.pop("long_message")

        code = d.pop("code")

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, UpdateEmailAddressResponse200VerificationType2ErrorType0Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = UpdateEmailAddressResponse200VerificationType2ErrorType0Meta.from_dict(_meta)

        clerk_trace_id = d.pop("clerk_trace_id", UNSET)

        update_email_address_response_200_verification_type_2_error_type_0 = cls(
            message=message,
            long_message=long_message,
            code=code,
            meta=meta,
            clerk_trace_id=clerk_trace_id,
        )

        update_email_address_response_200_verification_type_2_error_type_0.additional_properties = d
        return update_email_address_response_200_verification_type_2_error_type_0

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
