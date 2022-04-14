from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RoomModel:
    """
    Room model
    Attributes:
        room_id (str): The ID of the room.
        name (str): - The name of the room.
        canonical_alias (str): The canonical (main) alias address of the room.
        joined_members (int): How many users are currently in the room.
        joined_local_members (int): How many local users are currently in the room.
        version (str): The version of the room as a string.
        creator (str): The user_id of the room creator.
        encryption (str|None): Algorithm of end-to-end encryption of messages. Is null if encryption is not active.
        federatable (bool): Whether users on other servers can join this room.
        public (bool): Whether the room is visible in room directory.
        join_rules (str): The type of rules used for users wishing to join this room. One of: ["public", "knock", "invite", "private"].
        guest_access (str|None):  Whether guests can join the room. One of: ["can_join", "forbidden"].
        history_visibility (str): Who can see the room history. One of: ["invited", "joined", "shared", "world_readable"].
        state_events (int): Total number of state_events of a room. Complexity of the room.
    """

    room_id: str
    name: str
    canonical_alias: str
    joined_members: int
    joined_local_members: int
    version: str
    creator: str
    encryption: Optional[str]
    federatable: bool
    public: bool
    join_rules: str
    guest_access: Optional[str]
    history_visibility: str
    state_events: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RoomModel":
        return cls(**data)


@dataclass
class RoomsModel:
    """
    Rooms model
    Attributes:
        rooms (list[Room]): An array of objects, each containing information about a room
        offset (int): The offset of the first room in the list.
        total_rooms (int): The total number of rooms.
        next_batch (str|None): The token to get the next batch of rooms.
        prev_batch (str|None): The token to get the previous batch of rooms.
    """

    rooms: List[RoomModel]
    offset: int
    total_rooms: int
    next_batch: Optional[str] = None
    prev_batch: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RoomsModel":  # type: ignore
        data = data.copy()
        rooms = [RoomModel.from_dict(room) for room in data["rooms"]]
        del data["rooms"]
        return cls(**data, rooms=rooms)
