# Matrix Admin SDK

Async wrapper for the Matrix.org Admin API.

## Installation
```shell
pip install matrix-admin-sdk
```


## Usage
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
## Index
### Endpoints
#### v1
- [Account Validity](endpoints/v1/account_validity.md#Account Validity)
- [Background Updates](endpoints/v1/background_updates.md#Background Updates)
- [Delete Group](endpoints/v1/delete_group.md#Delete Group)
- [Delete Local Media](endpoints/v1/delete_local_media.md#Delete Local Media)
- [Edit Room Membership](endpoints/v1/edit_room_membership.md#Edit Room Membership)
- [Event Reports](endpoints/v1/event_reports.md#Event Reports)
- [Purge History](endpoints/v1/purge_history.md#Purge History)
- [Purge Remote Media](endpoints/v1/purge_remote_media.md#Purge Remote Media)
- [Quarantine Media](endpoints/v1/quarantine_media.md#Quarantine Media)
- [Querying Media](endpoints/v1/querying_media.md#Querying Media)
- [Register Users](endpoints/v1/register_user.md#Register Users)
- [Registration Tokens](endpoints/v1/registration_tokens.md#Registration Tokens)
- [Rooms](endpoints/v1/rooms.md#Rooms)
- [Forward Extremities](endpoints/v1/forward_extremities.md#Forward Extremities)
- [Server Notices](endpoints/v1/server_notices.md#Server Notices)
- [User Media Statistics](endpoints/v1/user_media_statistics.md#User Media Statistics)
- [User](endpoints/v1/user.md#User)
- [User Rate Limits](endpoints/v1/user_rate_limits.md#User Rate Limits)
- [Server](endpoints/v1/server.md#Server)
- [Federation](endpoints/v1/federation.md#Federation)
 
#### v2
- [Users](endpoints/v2/users.md#Users)
- [User Devices](endpoints/v2/users_devices.md#User Devices)
- [Rooms](endpoints/v2/rooms.md#Rooms)
