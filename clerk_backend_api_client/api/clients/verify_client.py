from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.verify_client_body import VerifyClientBody
from ...models.verify_client_response_200 import VerifyClientResponse200
from ...models.verify_client_response_400 import VerifyClientResponse400
from ...models.verify_client_response_401 import VerifyClientResponse401
from ...models.verify_client_response_404 import VerifyClientResponse404
from ...types import Response


def _get_kwargs(
    *,
    body: VerifyClientBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/clients/verify",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VerifyClientResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = VerifyClientResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = VerifyClientResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = VerifyClientResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyClientBody,
) -> Response[
    Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
]:
    """Verify a client

     Verifies the client in the provided token

    Args:
        body (VerifyClientBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyClientBody,
) -> Optional[
    Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
]:
    """Verify a client

     Verifies the client in the provided token

    Args:
        body (VerifyClientBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyClientBody,
) -> Response[
    Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
]:
    """Verify a client

     Verifies the client in the provided token

    Args:
        body (VerifyClientBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyClientBody,
) -> Optional[
    Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
]:
    """Verify a client

     Verifies the client in the provided token

    Args:
        body (VerifyClientBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VerifyClientResponse200, VerifyClientResponse400, VerifyClientResponse401, VerifyClientResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed