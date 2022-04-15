from urllib.parse import urljoin

from matrix_admin_sdk import MatrixAdminClient


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
