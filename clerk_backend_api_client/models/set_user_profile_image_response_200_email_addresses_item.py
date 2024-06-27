from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.set_user_profile_image_response_200_email_addresses_item_object import (
    SetUserProfileImageResponse200EmailAddressesItemObject,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_user_profile_image_response_200_email_addresses_item_linked_to_item import (
        SetUserProfileImageResponse200EmailAddressesItemLinkedToItem,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_0 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType0,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_1 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType1,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_2 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType2,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_0 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_1 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_2 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_0 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_1 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1,
    )
    from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_2 import (
        SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2,
    )


T = TypeVar("T", bound="SetUserProfileImageResponse200EmailAddressesItem")


@_attrs_define
class SetUserProfileImageResponse200EmailAddressesItem:
    """
    Attributes:
        object_ (SetUserProfileImageResponse200EmailAddressesItemObject): String representing the object's type. Objects
            of the same type share the same value.
        email_address (str):
        reserved (bool):
        verification (Union['SetUserProfileImageResponse200EmailAddressesItemVerificationType0',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType1',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType2',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1',
            'SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2']):
        linked_to (List['SetUserProfileImageResponse200EmailAddressesItemLinkedToItem']):
        created_at (int): Unix timestamp of creation
        updated_at (int): Unix timestamp of creation
        id (Union[Unset, str]):
    """

    object_: SetUserProfileImageResponse200EmailAddressesItemObject
    email_address: str
    reserved: bool
    verification: Union[
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType0",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType1",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType2",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1",
        "SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2",
    ]
    linked_to: List["SetUserProfileImageResponse200EmailAddressesItemLinkedToItem"]
    created_at: int
    updated_at: int
    id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_0 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType0,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_1 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType1,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_2 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType2,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_0 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_1 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_2 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_0 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_1 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1,
        )

        object_ = self.object_.value

        email_address = self.email_address

        reserved = self.reserved

        verification: Dict[str, Any]
        if isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType2):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1):
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "email_address": email_address,
                "reserved": reserved,
                "verification": verification,
                "linked_to": linked_to,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.set_user_profile_image_response_200_email_addresses_item_linked_to_item import (
            SetUserProfileImageResponse200EmailAddressesItemLinkedToItem,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_0 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType0,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_1 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType1,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_2 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType2,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_0 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_1 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_3_type_2 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_0 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_1 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1,
        )
        from ..models.set_user_profile_image_response_200_email_addresses_item_verification_type_4_type_2 import (
            SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2,
        )

        d = src_dict.copy()
        object_ = SetUserProfileImageResponse200EmailAddressesItemObject(d.pop("object"))

        email_address = d.pop("email_address")

        reserved = d.pop("reserved")

        def _parse_verification(
            data: object,
        ) -> Union[
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType0",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType1",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType2",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1",
            "SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_0 = SetUserProfileImageResponse200EmailAddressesItemVerificationType0.from_dict(data)

                return verification_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_1 = SetUserProfileImageResponse200EmailAddressesItemVerificationType1.from_dict(data)

                return verification_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2 = SetUserProfileImageResponse200EmailAddressesItemVerificationType2.from_dict(data)

                return verification_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_0 = (
                    SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type0.from_dict(data)
                )

                return verification_type_3_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_1 = (
                    SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type1.from_dict(data)
                )

                return verification_type_3_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_2 = (
                    SetUserProfileImageResponse200EmailAddressesItemVerificationType3Type2.from_dict(data)
                )

                return verification_type_3_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_4_type_0 = (
                    SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type0.from_dict(data)
                )

                return verification_type_4_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_4_type_1 = (
                    SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type1.from_dict(data)
                )

                return verification_type_4_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            verification_type_4_type_2 = (
                SetUserProfileImageResponse200EmailAddressesItemVerificationType4Type2.from_dict(data)
            )

            return verification_type_4_type_2

        verification = _parse_verification(d.pop("verification"))

        linked_to = []
        _linked_to = d.pop("linked_to")
        for linked_to_item_data in _linked_to:
            linked_to_item = SetUserProfileImageResponse200EmailAddressesItemLinkedToItem.from_dict(linked_to_item_data)

            linked_to.append(linked_to_item)

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        id = d.pop("id", UNSET)

        set_user_profile_image_response_200_email_addresses_item = cls(
            object_=object_,
            email_address=email_address,
            reserved=reserved,
            verification=verification,
            linked_to=linked_to,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
        )

        return set_user_profile_image_response_200_email_addresses_item
