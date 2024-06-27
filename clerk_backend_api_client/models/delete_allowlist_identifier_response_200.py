from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteAllowlistIdentifierResponse200")


@_attrs_define
class DeleteAllowlistIdentifierResponse200:
    """
    Attributes:
        object_ (str):
        deleted (bool):
        id (Union[Unset, str]):
        slug (Union[Unset, str]):
    """

    object_: str
    deleted: bool
    id: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_

        deleted = self.deleted

        id = self.id

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "deleted": deleted,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = d.pop("object")

        deleted = d.pop("deleted")

        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        delete_allowlist_identifier_response_200 = cls(
            object_=object_,
            deleted=deleted,
            id=id,
            slug=slug,
        )

        return delete_allowlist_identifier_response_200
