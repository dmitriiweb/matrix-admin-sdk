from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .base_model import BaseModel


@dataclass
class ConnectionModel(BaseModel):
    ip: str
    last_seen: int
    user_agent: str


@dataclass
class CurrentSessionsModel(BaseModel):
    user_id: str
    devices: Dict[str, List[ConnectionModel]]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CurrentSessionsModel":
        devices = {}
        for k, v in data["devices"].items():
            for session in v["sessions"]:
                devices[k] = [ConnectionModel(**i) for i in session["connections"]]
        return cls(
            user_id=data["user_id"],
            devices=devices,
        )


@dataclass
class RoomModel(BaseModel):
    """
    Room model
    Attributes:
        joined_rooms (list[str]): An array of room_id
        total (int): Number of rooms
    """

    joined_rooms: List[str]
    total: int


@dataclass
class MediaModel(BaseModel):
    created_ts: int
    media_id: str
    media_length: int
    media_type: str
    safe_from_quarantine: bool
    upload_name: str
    last_access_ts: Optional[int] = None
    quarantined_by: Optional[str] = None


@dataclass
class MediaListModel(BaseModel):
    media: List[MediaModel]
    next_token: Optional[int]
    total: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MediaListModel":
        media = [MediaModel.from_dict(i) for i in data["media"]]
        return cls(
            media=media,
            next_token=data.get("next_token"),
            total=data["total"],
        )


@dataclass
class DeletedMediaModel(BaseModel):
    """
    Deleted media model
    Attributes:
        deleted_media (list[str]): List of deleted media_id
        total (int): Total number of deleted media
    """

    deleted_media: List[str]
    total: int
