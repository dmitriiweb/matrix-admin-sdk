# Matrix Admin Sdk

Async wrapper for matrix.org admin API


## Installation

## Usage
Documentation: 

### Quick Start
```python
import asyncio

import httpx

from matrix_admin_sdk import MatrixAdminClient
from matrix_admin_sdk.endpoints.v1 import EditRoomMembership


async def main():
    admin_key = "admin_key"
    http_client = httpx.AsyncClient()
    server_url = "https://matrix.server.com"

    admin_client = MatrixAdminClient(http_client, admin_key, server_url)

    api = EditRoomMembership(admin_client)
    res = await api.join_user_to_room("room_id", "user_id")


if __name__ == "__main__":
    asyncio.run(main())
```