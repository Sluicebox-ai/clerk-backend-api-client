from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.create_phone_number_response_200_object import CreatePhoneNumberResponse200Object
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_phone_number_response_200_linked_to_item import CreatePhoneNumberResponse200LinkedToItem
    from ..models.create_phone_number_response_200_verification_type_0 import (
        CreatePhoneNumberResponse200VerificationType0,
    )
    from ..models.create_phone_number_response_200_verification_type_1 import (
        CreatePhoneNumberResponse200VerificationType1,
    )
    from ..models.create_phone_number_response_200_verification_type_2_type_0 import (
        CreatePhoneNumberResponse200VerificationType2Type0,
    )
    from ..models.create_phone_number_response_200_verification_type_2_type_1 import (
        CreatePhoneNumberResponse200VerificationType2Type1,
    )
    from ..models.create_phone_number_response_200_verification_type_3_type_0 import (
        CreatePhoneNumberResponse200VerificationType3Type0,
    )
    from ..models.create_phone_number_response_200_verification_type_3_type_1 import (
        CreatePhoneNumberResponse200VerificationType3Type1,
    )


T = TypeVar("T", bound="CreatePhoneNumberResponse200")


@_attrs_define
class CreatePhoneNumberResponse200:
    """
    Attributes:
        object_ (CreatePhoneNumberResponse200Object): String representing the object's type. Objects of the same type
            share the same value.
        phone_number (str):
        reserved (bool):
        verification (Union['CreatePhoneNumberResponse200VerificationType0',
            'CreatePhoneNumberResponse200VerificationType1', 'CreatePhoneNumberResponse200VerificationType2Type0',
            'CreatePhoneNumberResponse200VerificationType2Type1', 'CreatePhoneNumberResponse200VerificationType3Type0',
            'CreatePhoneNumberResponse200VerificationType3Type1']):
        linked_to (List['CreatePhoneNumberResponse200LinkedToItem']):
        created_at (int): Unix timestamp of creation
        updated_at (int): Unix timestamp of creation
        id (Union[Unset, str]):
        reserved_for_second_factor (Union[Unset, bool]):
        default_second_factor (Union[Unset, bool]):
        backup_codes (Union[List[str], None, Unset]):
    """

    object_: CreatePhoneNumberResponse200Object
    phone_number: str
    reserved: bool
    verification: Union[
        "CreatePhoneNumberResponse200VerificationType0",
        "CreatePhoneNumberResponse200VerificationType1",
        "CreatePhoneNumberResponse200VerificationType2Type0",
        "CreatePhoneNumberResponse200VerificationType2Type1",
        "CreatePhoneNumberResponse200VerificationType3Type0",
        "CreatePhoneNumberResponse200VerificationType3Type1",
    ]
    linked_to: List["CreatePhoneNumberResponse200LinkedToItem"]
    created_at: int
    updated_at: int
    id: Union[Unset, str] = UNSET
    reserved_for_second_factor: Union[Unset, bool] = UNSET
    default_second_factor: Union[Unset, bool] = UNSET
    backup_codes: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.create_phone_number_response_200_verification_type_0 import (
            CreatePhoneNumberResponse200VerificationType0,
        )
        from ..models.create_phone_number_response_200_verification_type_1 import (
            CreatePhoneNumberResponse200VerificationType1,
        )
        from ..models.create_phone_number_response_200_verification_type_2_type_0 import (
            CreatePhoneNumberResponse200VerificationType2Type0,
        )
        from ..models.create_phone_number_response_200_verification_type_2_type_1 import (
            CreatePhoneNumberResponse200VerificationType2Type1,
        )
        from ..models.create_phone_number_response_200_verification_type_3_type_0 import (
            CreatePhoneNumberResponse200VerificationType3Type0,
        )

        object_ = self.object_.value

        phone_number = self.phone_number

        reserved = self.reserved

        verification: Dict[str, Any]
        if isinstance(self.verification, CreatePhoneNumberResponse200VerificationType0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, CreatePhoneNumberResponse200VerificationType1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, CreatePhoneNumberResponse200VerificationType2Type0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, CreatePhoneNumberResponse200VerificationType2Type1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, CreatePhoneNumberResponse200VerificationType3Type0):
            verification = self.verification.to_dict()
        else:
            verification = self.verification.to_dict()

        linked_to = []
        for linked_to_item_data in self.linked_to:
            linked_to_item = linked_to_item_data.to_dict()
            linked_to.append(linked_to_item)

        created_at = self.created_at

        updated_at = self.updated_at

        id = self.id

        reserved_for_second_factor = self.reserved_for_second_factor

        default_second_factor = self.default_second_factor

        backup_codes: Union[List[str], None, Unset]
        if isinstance(self.backup_codes, Unset):
            backup_codes = UNSET
        elif isinstance(self.backup_codes, list):
            backup_codes = self.backup_codes

        else:
            backup_codes = self.backup_codes

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "phone_number": phone_number,
                "reserved": reserved,
                "verification": verification,
                "linked_to": linked_to,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if reserved_for_second_factor is not UNSET:
            field_dict["reserved_for_second_factor"] = reserved_for_second_factor
        if default_second_factor is not UNSET:
            field_dict["default_second_factor"] = default_second_factor
        if backup_codes is not UNSET:
            field_dict["backup_codes"] = backup_codes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_phone_number_response_200_linked_to_item import CreatePhoneNumberResponse200LinkedToItem
        from ..models.create_phone_number_response_200_verification_type_0 import (
            CreatePhoneNumberResponse200VerificationType0,
        )
        from ..models.create_phone_number_response_200_verification_type_1 import (
            CreatePhoneNumberResponse200VerificationType1,
        )
        from ..models.create_phone_number_response_200_verification_type_2_type_0 import (
            CreatePhoneNumberResponse200VerificationType2Type0,
        )
        from ..models.create_phone_number_response_200_verification_type_2_type_1 import (
            CreatePhoneNumberResponse200VerificationType2Type1,
        )
        from ..models.create_phone_number_response_200_verification_type_3_type_0 import (
            CreatePhoneNumberResponse200VerificationType3Type0,
        )
        from ..models.create_phone_number_response_200_verification_type_3_type_1 import (
            CreatePhoneNumberResponse200VerificationType3Type1,
        )

        d = src_dict.copy()
        object_ = CreatePhoneNumberResponse200Object(d.pop("object"))

        phone_number = d.pop("phone_number")

        reserved = d.pop("reserved")

        def _parse_verification(
            data: object,
        ) -> Union[
            "CreatePhoneNumberResponse200VerificationType0",
            "CreatePhoneNumberResponse200VerificationType1",
            "CreatePhoneNumberResponse200VerificationType2Type0",
            "CreatePhoneNumberResponse200VerificationType2Type1",
            "CreatePhoneNumberResponse200VerificationType3Type0",
            "CreatePhoneNumberResponse200VerificationType3Type1",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_0 = CreatePhoneNumberResponse200VerificationType0.from_dict(data)

                return verification_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_1 = CreatePhoneNumberResponse200VerificationType1.from_dict(data)

                return verification_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2_type_0 = CreatePhoneNumberResponse200VerificationType2Type0.from_dict(data)

                return verification_type_2_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2_type_1 = CreatePhoneNumberResponse200VerificationType2Type1.from_dict(data)

                return verification_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_0 = CreatePhoneNumberResponse200VerificationType3Type0.from_dict(data)

                return verification_type_3_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            verification_type_3_type_1 = CreatePhoneNumberResponse200VerificationType3Type1.from_dict(data)

            return verification_type_3_type_1

        verification = _parse_verification(d.pop("verification"))

        linked_to = []
        _linked_to = d.pop("linked_to")
        for linked_to_item_data in _linked_to:
            linked_to_item = CreatePhoneNumberResponse200LinkedToItem.from_dict(linked_to_item_data)

            linked_to.append(linked_to_item)

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        id = d.pop("id", UNSET)

        reserved_for_second_factor = d.pop("reserved_for_second_factor", UNSET)

        default_second_factor = d.pop("default_second_factor", UNSET)

        def _parse_backup_codes(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backup_codes_type_0 = cast(List[str], data)

                return backup_codes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        backup_codes = _parse_backup_codes(d.pop("backup_codes", UNSET))

        create_phone_number_response_200 = cls(
            object_=object_,
            phone_number=phone_number,
            reserved=reserved,
            verification=verification,
            linked_to=linked_to,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            reserved_for_second_factor=reserved_for_second_factor,
            default_second_factor=default_second_factor,
            backup_codes=backup_codes,
        )

        return create_phone_number_response_200
