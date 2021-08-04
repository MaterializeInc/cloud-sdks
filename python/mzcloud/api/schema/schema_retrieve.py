from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...types import UNSET, Unset
from ...models.schema_retrieve_response_200 import SchemaRetrieveResponse200
from typing import Dict
from typing import cast
from typing import Union
from ...models.schema_retrieve_format import SchemaRetrieveFormat



def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SchemaRetrieveFormat] = UNSET,

) -> Dict[str, Any]:
    url = "{}/api/schema".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params: Dict[str, Any] = {
        "format": json_format_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SchemaRetrieveResponse200]:
    if response.status_code == 200:
        response_200 = SchemaRetrieveResponse200.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SchemaRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SchemaRetrieveFormat] = UNSET,

) -> Response[SchemaRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
format_=format_,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SchemaRetrieveFormat] = UNSET,

) -> Optional[SchemaRetrieveResponse200]:
    """ OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json """

    return sync_detailed(
        client=client,
format_=format_,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SchemaRetrieveFormat] = UNSET,

) -> Response[SchemaRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
format_=format_,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, SchemaRetrieveFormat] = UNSET,

) -> Optional[SchemaRetrieveResponse200]:
    """ OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json """

    return (await asyncio_detailed(
        client=client,
format_=format_,

    )).parsed
