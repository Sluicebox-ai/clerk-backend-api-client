from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_saml_connection_body import CreateSAMLConnectionBody
from ...models.create_saml_connection_response_200 import CreateSAMLConnectionResponse200
from ...models.create_saml_connection_response_402 import CreateSAMLConnectionResponse402
from ...models.create_saml_connection_response_403 import CreateSAMLConnectionResponse403
from ...models.create_saml_connection_response_422 import CreateSAMLConnectionResponse422
from ...types import Response


def _get_kwargs(
    *,
    body: CreateSAMLConnectionBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/saml_connections",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateSAMLConnectionResponse200,
        CreateSAMLConnectionResponse402,
        CreateSAMLConnectionResponse403,
        CreateSAMLConnectionResponse422,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateSAMLConnectionResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = CreateSAMLConnectionResponse402.from_dict(response.json())

        return response_402
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = CreateSAMLConnectionResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = CreateSAMLConnectionResponse422.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateSAMLConnectionResponse200,
        CreateSAMLConnectionResponse402,
        CreateSAMLConnectionResponse403,
        CreateSAMLConnectionResponse422,
    ]
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
    body: CreateSAMLConnectionBody,
) -> Response[
    Union[
        CreateSAMLConnectionResponse200,
        CreateSAMLConnectionResponse402,
        CreateSAMLConnectionResponse403,
        CreateSAMLConnectionResponse422,
    ]
]:
    """Create a SAML Connection

     Create a new SAML Connection.

    Args:
        body (CreateSAMLConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateSAMLConnectionResponse200, CreateSAMLConnectionResponse402, CreateSAMLConnectionResponse403, CreateSAMLConnectionResponse422]]
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
    body: CreateSAMLConnectionBody,
) -> Optional[
    Union[
        CreateSAMLConnectionResponse200,
        CreateSAMLConnectionResponse402,
        CreateSAMLConnectionResponse403,
        CreateSAMLConnectionResponse422,
    ]
]:
    """Create a SAML Connection

     Create a new SAML Connection.

    Args:
        body (CreateSAMLConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSAMLConnectionResponse200, CreateSAMLConnectionResponse402, CreateSAMLConnectionResponse403, CreateSAMLConnectionResponse422]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateSAMLConnectionBody,
) -> Response[
    Union[
        CreateSAMLConnectionResponse200,
        CreateSAMLConnectionResponse402,
        CreateSAMLConnectionResponse403,
        CreateSAMLConnectionResponse422,
    ]
]:
    """Create a SAML Connection

     Create a new SAML Connection.

    Args:
        body (CreateSAMLConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateSAMLConnectionResponse200, CreateSAMLConnectionResponse402, CreateSAMLConnectionResponse403, CreateSAMLConnectionResponse422]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateSAMLConnectionBody,
) -> Optional[
    Union[
        CreateSAMLConnectionResponse200,
        CreateSAMLConnectionResponse402,
        CreateSAMLConnectionResponse403,
        CreateSAMLConnectionResponse422,
    ]
]:
    """Create a SAML Connection

     Create a new SAML Connection.

    Args:
        body (CreateSAMLConnectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSAMLConnectionResponse200, CreateSAMLConnectionResponse402, CreateSAMLConnectionResponse403, CreateSAMLConnectionResponse422]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
