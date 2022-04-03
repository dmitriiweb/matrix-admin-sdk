from matrix_admin_sdk import MatrixAdminClient


def test_client(matrix_admin_client: MatrixAdminClient):
    assert matrix_admin_client.access_token == "Bearer test_token"
    assert matrix_admin_client.request_headers == {"Authorization": "Bearer test_token"}
