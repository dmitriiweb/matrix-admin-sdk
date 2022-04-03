import pytest

from httpx import AsyncClient

from matrix_admin_sdk import MatrixAdminClient


@pytest.fixture()
async def matrix_admin_client() -> MatrixAdminClient:
    http_client = AsyncClient()
    mac = MatrixAdminClient(
        http_client=http_client,  # type: ignore
        access_token="test_token",
        server_url="https://test_url",
    )
    yield mac
    await http_client.aclose()
