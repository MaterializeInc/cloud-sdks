from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import Dict
from typing import cast
from ...models.patched_deployment_request import PatchedDeploymentRequest
from ...models.deployment import Deployment



def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: str,
    json_body: PatchedDeploymentRequest,

) -> Dict[str, Any]:
    url = "{}/api/deployments/{id}".format(
        client.base_url,id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Deployment]:
    if response.status_code == 200:
        response_200 = Deployment.from_dict(response.json())



        return response_200
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
    id: str,
    json_body: PatchedDeploymentRequest,

) -> Response[Deployment]:
    kwargs = _get_kwargs(
        client=client,
id=id,
json_body=json_body,

    )

    response = httpx.patch(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    json_body: PatchedDeploymentRequest,

) -> Optional[Deployment]:
    """ Partially update a deployment. """

    return sync_detailed(
        client=client,
id=id,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    json_body: PatchedDeploymentRequest,

) -> Response[Deployment]:
    kwargs = _get_kwargs(
        client=client,
id=id,
json_body=json_body,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.patch(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    json_body: PatchedDeploymentRequest,

) -> Optional[Deployment]:
    """ Partially update a deployment. """

    return (await asyncio_detailed(
        client=client,
id=id,
json_body=json_body,

    )).parsed
