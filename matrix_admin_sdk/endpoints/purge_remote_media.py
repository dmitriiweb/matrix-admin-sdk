from typing import Any, Dict

from .endpoint import Endpoint


class PurgeRemoteMedia(Endpoint):
    """
    The purge remote media API allows server admins to purge old cached remote media.
    """

    async def purge_remove_media(self, unix_timestamp_in_ms: int) -> Dict[Any, Any]:
        """
        The purge remote media API allows server admins to purge old cached
        remote media.
        Args:
            unix_timestamp_in_ms: Unix timestamp in milliseconds. All cached media that was
                last accessed before this timestamp will be removed.

        Returns:{"deleted": 10}

        """
        url = self.url(f"purge_media_cache?before_ts={unix_timestamp_in_ms}")
        response = await self.admin_client.post(url, {})
        return response.json()
