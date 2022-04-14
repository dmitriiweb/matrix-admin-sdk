from typing import Any, Dict, Optional

from .endpoint import Endpoint


class PurgeHistory(Endpoint):
    """
    The purge history API allows server admins to purge historic events from
    their database, reclaiming disk space.

    Depending on the amount of history being purged a call to the API may take
    several minutes or longer. During this period users will not be able to paginate
    further back in the room from the point being purged from.
    """

    async def purge_room_history(
        self,
        room_id: str,
        event_id: str,
        delete_local_events: bool = False,
        purge_up_to_event_id: Optional[str] = None,
        purge_up_to_ts: Optional[int] = None,
    ) -> Dict[str, str]:
        """
        By default, events sent by local users are not deleted, as they may
        represent the only copies of this content in existence. (Events sent by
        remote users are deleted.)

        Room state data (such as joins, leaves, topic) is always preserved.

        To delete local message events as well, set delete_local_events in the body

        The caller must specify the point in the room to purge up to. This can be
        specified by including an event_id in the URI, or by setting
        a purge_up_to_event_id or purge_up_to_ts in the request body.
        If an event id is given, that event (and others at the same graph depth)
        will be retained. If purge_up_to_ts is given, it should be a timestamp since
        the unix epoch, in milliseconds.

        The API starts the purge running, and returns immediately with a
        JSON body with a purge id

        Args:
            room_id: room id to purge history for
            event_id: event id
            delete_local_events: To delete local message events, Default: False
            purge_up_to_event_id
            purge_up_to_ts

        Returns: {"purge_id": "<opaque id>"}

        """
        url = f"/_synapse/admin/v1/purge_history/{room_id}/{event_id}]"
        data: Dict[str, Any] = {
            "delete_local_events": delete_local_events,
        }
        if purge_up_to_event_id is not None:
            data["purge_up_to_event_id"] = purge_up_to_event_id
        if purge_up_to_ts is not None:
            data["purge_up_to_ts"] = purge_up_to_ts

        response = await self.admin_client.post(url, data=data)

        return response.json()

    async def purge_status_query(self, purge_id: str) -> Dict[str, str]:
        """
        It is possible to poll for updates on recent purges
        Args:
            purge_id:

        Returns: {"status": "active"}. The status will be one of active,
            complete, or failed. If status is failed there will be a string
            error with the error message.

        """
        url = f"/_synapse/admin/v1/purge_history_status/{purge_id}"
        response = await self.admin_client.get(url)
        return response.json()
