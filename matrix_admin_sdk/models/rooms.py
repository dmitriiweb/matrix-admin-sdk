from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RoomModel:
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
    rooms: List[RoomModel]
    offset: int
    total_rooms: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RoomsModel":  # type: ignore
        data = data.copy()
        rooms = [RoomModel.from_dict(room) for room in data["rooms"]]
        del data["rooms"]
        return cls(**data, rooms=rooms)
