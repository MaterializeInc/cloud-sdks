from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.deployment import Deployment
from ...models.deployment_request import DeploymentRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: DeploymentRequest,
) -> Dict[str, Any]:
    url = "{}/api/deployments".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Deployment]:
    if response.status_code == 201:
        response_201 = Deployment.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Deployment]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DeploymentRequest,
) -> Response[Deployment]:
    """Create a new deployment.

    Args:
        json_body (DeploymentRequest):

    Returns:
        Response[Deployment]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: DeploymentRequest,
) -> Optional[Deployment]:
    """Create a new deployment.

    Args:
        json_body (DeploymentRequest):

    Returns:
        Response[Deployment]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DeploymentRequest,
) -> Response[Deployment]:
    """Create a new deployment.

    Args:
        json_body (DeploymentRequest):

    Returns:
        Response[Deployment]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: DeploymentRequest,
) -> Optional[Deployment]:
    """Create a new deployment.

    Args:
        json_body (DeploymentRequest):

    Returns:
        Response[Deployment]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
