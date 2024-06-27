from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_actor_token_response_200 import RevokeActorTokenResponse200
from ...models.revoke_actor_token_response_400 import RevokeActorTokenResponse400
from ...models.revoke_actor_token_response_404 import RevokeActorTokenResponse404
from ...types import Response


def _get_kwargs(
    actor_token_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/actor_tokens/{actor_token_id}/revoke",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RevokeActorTokenResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RevokeActorTokenResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = RevokeActorTokenResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    actor_token_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]:
    """Revoke actor token

     Revokes a pending actor token.

    Args:
        actor_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]
    """

    kwargs = _get_kwargs(
        actor_token_id=actor_token_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    actor_token_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]:
    """Revoke actor token

     Revokes a pending actor token.

    Args:
        actor_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]
    """

    return sync_detailed(
        actor_token_id=actor_token_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    actor_token_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]:
    """Revoke actor token

     Revokes a pending actor token.

    Args:
        actor_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]
    """

    kwargs = _get_kwargs(
        actor_token_id=actor_token_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    actor_token_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]]:
    """Revoke actor token

     Revokes a pending actor token.

    Args:
        actor_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RevokeActorTokenResponse200, RevokeActorTokenResponse400, RevokeActorTokenResponse404]
    """

    return (
        await asyncio_detailed(
            actor_token_id=actor_token_id,
            client=client,
        )
    ).parsed