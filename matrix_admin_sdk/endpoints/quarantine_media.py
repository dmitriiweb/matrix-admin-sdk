from typing import Any, Dict

from .endpoint import Endpoint


class QuarantineMedia(Endpoint):
    """
    Quarantining media means that it is marked as inaccessible by users.
    It applies to any local media, and any locally-cached copies of remote media.

    The media file itself (and any thumbnails) is not deleted from the server.
    """

    async def quarantining_media_by_id(
        self, server_name: str, media_id: str
    ) -> Dict[Any, Any]:
        """
        This API quarantines a single piece of local or remote media.
        Args:
            server_name: e.g. example.org
            media_id: e.g. abcdefg12345...

        Returns: dictionary
        """
        url = f"/_synapse/admin/v1/media/quarantine/{server_name}/{media_id}"
        response = await self.admin_client.post(url, {})
        return response.json()

    async def remove_media_from_quarantine_by_id(
        self, server_name: str, media_id: str
    ) -> Dict[Any, Any]:
        """
        This API removes a single piece of local or remote media from quarantine.
        Args:
            server_name: e.g. example.org
            media_id: e.g. abcdefg12345...

        Returns: dictionary
        """
        url = f"/_synapse/admin/v1/media/unquarantine/{server_name}/{media_id}"
        response = await self.admin_client.post(url, {})
        return response.json()

    async def quarantining_media_in_room(self, room_id) -> Dict[str, int]:
        """
        This API quarantines all local and remote media in a room.
        Args:
            room_id: e.g. !roomid12345:example.org

        Returns: {"num_quarantined": 10}
        """
        url = f"/_synapse/admin/v1/room/{room_id}/media/quarantine"
        response = await self.admin_client.post(url, {})
        return response.json()

    async def quarantining_all_media_of_user(self, user_id: str) -> Dict[str, int]:
        """
        This API quarantines all local media that a local user has uploaded.
        That is to say, if you would like to quarantine media uploaded by
        a user on a remote homeserver, you should instead use one of the other APIs.
        Args:
            user_id: User ID in the form of @bob:example.org

        Returns: {"num_quarantined": 10}

        """
        url = f"/_synapse/admin/v1/user/{user_id}/media/quarantine"
        response = await self.admin_client.post(url, {})
        return response.json()

    async def protecting_media_from_being_quarantined(
        self, media_id: str
    ) -> Dict[Any, Any]:
        """
        This API protects a single piece of local media from being quarantined using
        the above APIs. This is useful for sticker packs and other shared media
        which you do not want to get quarantined, especially when quarantining
        media in a room.
        Args:
            media_id: in the form of abcdefg12345...

        Returns: dictionary
        """
        url = f"/_synapse/admin/v1/media/protect/{media_id}"
        response = await self.admin_client.post(url, {})
        return response.json()

    async def unprotecting_media_from_being_quarantined(
        self, media_id: str
    ) -> Dict[Any, Any]:
        """
        This API protects a single piece of local media from being quarantined using
        the above APIs. This is useful for sticker packs and other shared media
        which you do not want to get quarantined, especially when quarantining
        media in a room.
        Args:
            media_id: in the form of abcdefg12345...

        Returns: dictionary
        """
        url = f"/_synapse/admin/v1/media/unprotect/{media_id}"
        response = await self.admin_client.post(url, {})
        return response.json()
