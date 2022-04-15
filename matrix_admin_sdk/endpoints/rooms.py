from enum import Enum
from typing import Optional

from matrix_admin_sdk.models.rooms import RoomMembersModel, RoomModel, RoomsModel

from .endpoint import Endpoint, RequestMethods


class OrderBy(Enum):
    """
    Enum for the order by parameter

    Attributes:
        NAME: Rooms are ordered alphabetically by room name. This is the default.
        CANONICAL_ALIAS: Rooms are ordered alphabetically by main alias address of the room.
        JOINED_LOCAL_MEMBERS: Rooms are ordered by the number of members. Largest to smallest.
        JOINED_LOCAL_MEMBERS: Rooms are ordered by the number of local members. Largest to smallest.
        VERSION: Rooms are ordered by room version. Largest to smallest.
        CREATOR: Rooms are ordered alphabetically by creator of the room.
        ENCRYPTION: Rooms are ordered alphabetically by the end-to-end encryption algorithm.
        FEDERATABLE: Rooms are ordered by whether the room is federatable.
        PUBLIC: Rooms are ordered by visibility in room list.
        JOIN_RULES: Rooms are ordered alphabetically by join rules of the room.
        GUEST_ACCESS: Rooms are ordered alphabetically by guest access option of the room.
        HISTORY_VISIBILITY: Rooms are ordered alphabetically by visibility of history of the room.
        STATE_EVENTS: Rooms are ordered by number of state events. Largest to smallest.
    """

    NAME = "name"
    CANONICAL_ALIAS = "canonical_alias"
    JOINED_MEMBERS = "joined_members"
    JOINED_LOCAL_MEMBERS = "joined_local_members"
    VERSION = "version"
    CREATOR = "creator"
    ENCRYPTION = "encryption"
    FEDERATABLE = "federatable"
    PUBLIC = "public"
    JOIN_RULES = "join_rules"
    GUEST_ACCESS = "guest_access"
    HISTORY_VISIBILITY = "history_visibility"
    STATE_EVENTS = "state_events"


class Rooms(Endpoint):
    """
    Rooms Endpoints API
    """

    async def list_rooms(
        self,
        from_: int = 0,
        limit: int = 100,
        order_by: Optional[OrderBy] = None,
        dir_: str = "f",
        search_term: Optional[str] = None,
    ) -> RoomsModel:
        """
        The List Room admin API allows server admins to get a list of rooms on
        their server. There are various parameters available that allow for
        filtering and sorting the returned list. This API supports pagination.

        Args:
            from_: Offset in the returned list. Defaults to 0
            limit: Maximum amount of rooms to return. Defaults to 100.
            order_by: The method in which to sort the returned list of rooms.
                Defaults to OrderBy.NAME.
            dir_: Direction of room order. Either f for forwards or b for backwards.
                Setting this value to b will reverse the above sort order. Defaults to f
            search_term: Filter rooms by their room name, canonical alias and
                room id. Specifically, rooms are selected if the search term is
                contained in: the room's name, the local part of the room's canonical alias,
                or the complete (local and server part) room's id (case sensitive).
                Defaults to no filtering.

        Returns:

        """
        if order_by is None:
            order_by = OrderBy.NAME
        if dir_ not in ("f", "b"):
            raise ValueError("dir_ must be either f or b")

        url = self.url("rooms")
        params = {
            "from": from_,
            "limit": limit,
            "order_by": order_by.name,
            "dir": dir_,
        }
        if search_term is not None:
            params["search_term"] = search_term

        result = await self.request(RequestMethods.GET, url, params=params)
        return RoomsModel.from_dict(result)

    async def room_details(self, room_id: str) -> RoomModel:
        """
        The Room Details admin API allows server admins to get all details of a room.
        Args:
            room_id: The room id to get details for.

        Returns:

        """
        url = self.url(f"rooms/{room_id}")
        result = await self.request(RequestMethods.GET, url)
        res: RoomModel = RoomModel.from_dict(result)
        return res

    async def room_members(self, room_id: str) -> RoomMembersModel:
        """
        The Room Members admin API allows server admins to get a list of all
        members of a room.
        Args:
            room_id: The room id to get details for.

        Returns: RoomMembersModel

        """
        url = self.url(f"rooms/{room_id}/members")
        result = await self.request(RequestMethods.GET, url)
        res: RoomMembersModel = RoomMembersModel.from_dict(result)
        return res
