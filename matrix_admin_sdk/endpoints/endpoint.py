from matrix_admin_sdk import MatrixAdminClient


class Endpoint:
    """
    Base class for all endpoints.
    """

    def __init__(self, admin_client: MatrixAdminClient):
        """
        Initialize the endpoint.
        Args:
            admin_client: MatrixAdminClient instance.
        """
        self.admin_client = admin_client
