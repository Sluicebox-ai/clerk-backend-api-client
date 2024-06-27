from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unban_user_response_200 import UnbanUserResponse200
from ...models.unban_user_response_402 import UnbanUserResponse402
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/users/{user_id}/unban",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[UnbanUserResponse200, UnbanUserResponse402]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UnbanUserResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = UnbanUserResponse402.from_dict(response.json())

        return response_402
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[UnbanUserResponse200, UnbanUserResponse402]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[UnbanUserResponse200, UnbanUserResponse402]]:
    """Unban a user

     Removes the ban mark from the given user.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UnbanUserResponse200, UnbanUserResponse402]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[UnbanUserResponse200, UnbanUserResponse402]]:
    """Unban a user

     Removes the ban mark from the given user.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UnbanUserResponse200, UnbanUserResponse402]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[UnbanUserResponse200, UnbanUserResponse402]]:
    """Unban a user

     Removes the ban mark from the given user.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UnbanUserResponse200, UnbanUserResponse402]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[UnbanUserResponse200, UnbanUserResponse402]]:
    """Unban a user

     Removes the ban mark from the given user.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UnbanUserResponse200, UnbanUserResponse402]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed