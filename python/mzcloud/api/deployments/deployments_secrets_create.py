from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    secret: str,
    *,
    client: AuthenticatedClient,
    json_body: str,
) -> Dict[str, Any]:
    url = "{}/api/deployments/{id}/secrets/{secret}".format(client.base_url, id=id, secret=secret)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: str,
) -> Response[Any]:
    """Insert/update a customer defined secret in the deployment

    Args:
        id (str):
        secret (str):
        json_body (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        secret=secret,
        client=client,
        json_body=json_body,
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
    json_body: str,
) -> Response[Any]:
    """Insert/update a customer defined secret in the deployment

    Args:
        id (str):
        secret (str):
        json_body (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        secret=secret,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
