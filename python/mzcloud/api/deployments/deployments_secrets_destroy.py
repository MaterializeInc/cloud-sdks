from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    secret: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/deployments/{id}/secrets/{secret}".format(client.base_url, id=id, secret=secret)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    secret: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete a customer defined secret from the deployment

    Args:
        id (str):
        secret (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        secret=secret,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    secret: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete a customer defined secret from the deployment

    Args:
        id (str):
        secret (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        secret=secret,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
