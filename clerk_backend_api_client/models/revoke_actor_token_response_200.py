from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.revoke_actor_token_response_200_object import RevokeActorTokenResponse200Object
from ..models.revoke_actor_token_response_200_status import RevokeActorTokenResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revoke_actor_token_response_200_actor import RevokeActorTokenResponse200Actor


T = TypeVar("T", bound="RevokeActorTokenResponse200")


@_attrs_define
class RevokeActorTokenResponse200:
    """
    Attributes:
        object_ (RevokeActorTokenResponse200Object):
        id (str):
        status (RevokeActorTokenResponse200Status):
        user_id (str):
        actor (RevokeActorTokenResponse200Actor):
        created_at (int): Unix timestamp of creation.
        updated_at (int): Unix timestamp of last update.
        token (Union[None, Unset, str]):
        url (Union[None, Unset, str]):
    """

    object_: RevokeActorTokenResponse200Object
    id: str
    status: RevokeActorTokenResponse200Status
    user_id: str
    actor: "RevokeActorTokenResponse200Actor"
    created_at: int
    updated_at: int
    token: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        status = self.status.value

        user_id = self.user_id

        actor = self.actor.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        token: Union[None, Unset, str]
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "status": status,
                "user_id": user_id,
                "actor": actor,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.revoke_actor_token_response_200_actor import RevokeActorTokenResponse200Actor

        d = src_dict.copy()
        object_ = RevokeActorTokenResponse200Object(d.pop("object"))

        id = d.pop("id")

        status = RevokeActorTokenResponse200Status(d.pop("status"))

        user_id = d.pop("user_id")

        actor = RevokeActorTokenResponse200Actor.from_dict(d.pop("actor"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        token = _parse_token(d.pop("token", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        revoke_actor_token_response_200 = cls(
            object_=object_,
            id=id,
            status=status,
            user_id=user_id,
            actor=actor,
            created_at=created_at,
            updated_at=updated_at,
            token=token,
            url=url,
        )

        return revoke_actor_token_response_200
