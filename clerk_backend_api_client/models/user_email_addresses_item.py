from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.user_email_addresses_item_object import UserEmailAddressesItemObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_email_addresses_item_linked_to_item import UserEmailAddressesItemLinkedToItem
    from ..models.user_email_addresses_item_verification_type_0 import UserEmailAddressesItemVerificationType0
    from ..models.user_email_addresses_item_verification_type_1 import UserEmailAddressesItemVerificationType1
    from ..models.user_email_addresses_item_verification_type_2 import UserEmailAddressesItemVerificationType2
    from ..models.user_email_addresses_item_verification_type_3_type_0 import (
        UserEmailAddressesItemVerificationType3Type0,
    )
    from ..models.user_email_addresses_item_verification_type_3_type_1 import (
        UserEmailAddressesItemVerificationType3Type1,
    )
    from ..models.user_email_addresses_item_verification_type_3_type_2 import (
        UserEmailAddressesItemVerificationType3Type2,
    )
    from ..models.user_email_addresses_item_verification_type_4_type_0 import (
        UserEmailAddressesItemVerificationType4Type0,
    )
    from ..models.user_email_addresses_item_verification_type_4_type_1 import (
        UserEmailAddressesItemVerificationType4Type1,
    )
    from ..models.user_email_addresses_item_verification_type_4_type_2 import (
        UserEmailAddressesItemVerificationType4Type2,
    )


T = TypeVar("T", bound="UserEmailAddressesItem")


@_attrs_define
class UserEmailAddressesItem:
    """
    Attributes:
        object_ (UserEmailAddressesItemObject): String representing the object's type. Objects of the same type share
            the same value.
        email_address (str):
        reserved (bool):
        verification (Union['UserEmailAddressesItemVerificationType0', 'UserEmailAddressesItemVerificationType1',
            'UserEmailAddressesItemVerificationType2', 'UserEmailAddressesItemVerificationType3Type0',
            'UserEmailAddressesItemVerificationType3Type1', 'UserEmailAddressesItemVerificationType3Type2',
            'UserEmailAddressesItemVerificationType4Type0', 'UserEmailAddressesItemVerificationType4Type1',
            'UserEmailAddressesItemVerificationType4Type2']):
        linked_to (List['UserEmailAddressesItemLinkedToItem']):
        created_at (int): Unix timestamp of creation
        updated_at (int): Unix timestamp of creation
        id (Union[Unset, str]):
    """

    object_: UserEmailAddressesItemObject
    email_address: str
    reserved: bool
    verification: Union[
        "UserEmailAddressesItemVerificationType0",
        "UserEmailAddressesItemVerificationType1",
        "UserEmailAddressesItemVerificationType2",
        "UserEmailAddressesItemVerificationType3Type0",
        "UserEmailAddressesItemVerificationType3Type1",
        "UserEmailAddressesItemVerificationType3Type2",
        "UserEmailAddressesItemVerificationType4Type0",
        "UserEmailAddressesItemVerificationType4Type1",
        "UserEmailAddressesItemVerificationType4Type2",
    ]
    linked_to: List["UserEmailAddressesItemLinkedToItem"]
    created_at: int
    updated_at: int
    id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.user_email_addresses_item_verification_type_0 import UserEmailAddressesItemVerificationType0
        from ..models.user_email_addresses_item_verification_type_1 import UserEmailAddressesItemVerificationType1
        from ..models.user_email_addresses_item_verification_type_2 import UserEmailAddressesItemVerificationType2
        from ..models.user_email_addresses_item_verification_type_3_type_0 import (
            UserEmailAddressesItemVerificationType3Type0,
        )
        from ..models.user_email_addresses_item_verification_type_3_type_1 import (
            UserEmailAddressesItemVerificationType3Type1,
        )
        from ..models.user_email_addresses_item_verification_type_3_type_2 import (
            UserEmailAddressesItemVerificationType3Type2,
        )
        from ..models.user_email_addresses_item_verification_type_4_type_0 import (
            UserEmailAddressesItemVerificationType4Type0,
        )
        from ..models.user_email_addresses_item_verification_type_4_type_1 import (
            UserEmailAddressesItemVerificationType4Type1,
        )

        object_ = self.object_.value

        email_address = self.email_address

        reserved = self.reserved

        verification: Dict[str, Any]
        if isinstance(self.verification, UserEmailAddressesItemVerificationType0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, UserEmailAddressesItemVerificationType1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, UserEmailAddressesItemVerificationType2):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, UserEmailAddressesItemVerificationType3Type0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, UserEmailAddressesItemVerificationType3Type1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, UserEmailAddressesItemVerificationType3Type2):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, UserEmailAddressesItemVerificationType4Type0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, UserEmailAddressesItemVerificationType4Type1):
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
        from ..models.user_email_addresses_item_linked_to_item import UserEmailAddressesItemLinkedToItem
        from ..models.user_email_addresses_item_verification_type_0 import UserEmailAddressesItemVerificationType0
        from ..models.user_email_addresses_item_verification_type_1 import UserEmailAddressesItemVerificationType1
        from ..models.user_email_addresses_item_verification_type_2 import UserEmailAddressesItemVerificationType2
        from ..models.user_email_addresses_item_verification_type_3_type_0 import (
            UserEmailAddressesItemVerificationType3Type0,
        )
        from ..models.user_email_addresses_item_verification_type_3_type_1 import (
            UserEmailAddressesItemVerificationType3Type1,
        )
        from ..models.user_email_addresses_item_verification_type_3_type_2 import (
            UserEmailAddressesItemVerificationType3Type2,
        )
        from ..models.user_email_addresses_item_verification_type_4_type_0 import (
            UserEmailAddressesItemVerificationType4Type0,
        )
        from ..models.user_email_addresses_item_verification_type_4_type_1 import (
            UserEmailAddressesItemVerificationType4Type1,
        )
        from ..models.user_email_addresses_item_verification_type_4_type_2 import (
            UserEmailAddressesItemVerificationType4Type2,
        )

        d = src_dict.copy()
        object_ = UserEmailAddressesItemObject(d.pop("object"))

        email_address = d.pop("email_address")

        reserved = d.pop("reserved")

        def _parse_verification(
            data: object,
        ) -> Union[
            "UserEmailAddressesItemVerificationType0",
            "UserEmailAddressesItemVerificationType1",
            "UserEmailAddressesItemVerificationType2",
            "UserEmailAddressesItemVerificationType3Type0",
            "UserEmailAddressesItemVerificationType3Type1",
            "UserEmailAddressesItemVerificationType3Type2",
            "UserEmailAddressesItemVerificationType4Type0",
            "UserEmailAddressesItemVerificationType4Type1",
            "UserEmailAddressesItemVerificationType4Type2",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_0 = UserEmailAddressesItemVerificationType0.from_dict(data)

                return verification_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_1 = UserEmailAddressesItemVerificationType1.from_dict(data)

                return verification_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2 = UserEmailAddressesItemVerificationType2.from_dict(data)

                return verification_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_0 = UserEmailAddressesItemVerificationType3Type0.from_dict(data)

                return verification_type_3_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_1 = UserEmailAddressesItemVerificationType3Type1.from_dict(data)

                return verification_type_3_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_2 = UserEmailAddressesItemVerificationType3Type2.from_dict(data)

                return verification_type_3_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_4_type_0 = UserEmailAddressesItemVerificationType4Type0.from_dict(data)

                return verification_type_4_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_4_type_1 = UserEmailAddressesItemVerificationType4Type1.from_dict(data)

                return verification_type_4_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            verification_type_4_type_2 = UserEmailAddressesItemVerificationType4Type2.from_dict(data)

            return verification_type_4_type_2

        verification = _parse_verification(d.pop("verification"))

        linked_to = []
        _linked_to = d.pop("linked_to")
        for linked_to_item_data in _linked_to:
            linked_to_item = UserEmailAddressesItemLinkedToItem.from_dict(linked_to_item_data)

            linked_to.append(linked_to_item)

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        id = d.pop("id", UNSET)

        user_email_addresses_item = cls(
            object_=object_,
            email_address=email_address,
            reserved=reserved,
            verification=verification,
            linked_to=linked_to,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
        )

        return user_email_addresses_item
