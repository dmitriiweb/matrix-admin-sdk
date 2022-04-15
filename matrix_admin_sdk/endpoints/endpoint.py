from enum import Enum, auto
from typing import Any, Awaitable, Callable, Dict, Protocol
from urllib.parse import urljoin

from matrix_admin_sdk import MatrixAdminClient


class Response(Protocol):
    status_code: int
    text: str

    def json(self) -> Dict[str, Any]:
        ...


class RequestMethods(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()


RequestFunc = Callable[..., Awaitable[Response]]


class Endpoint:
    """
    Base class for all endpoints.
    """

    base_url = "/_synapse/admin/v1/"

    def __init__(self, admin_client: MatrixAdminClient):
        """
        Initialize the endpoint.
        Args:
            admin_client: MatrixAdminClient instance.
        """
        self.admin_client = admin_client

    def url(self, endpoint: str) -> str:
        return urljoin(self.base_url, endpoint)

    async def request(
        self, /, method: RequestMethods, url: str, **kwargs
    ) -> Dict[str, Any]:
        methods: Dict[RequestMethods, RequestFunc] = {
            RequestMethods.GET: self.admin_client.get,
            RequestMethods.POST: self.admin_client.post,
            RequestMethods.PUT: self.admin_client.put,
            RequestMethods.DELETE: self.admin_client.delete,
        }
        req = methods[method]
        response = await req(url, **kwargs)
        return response.json()
