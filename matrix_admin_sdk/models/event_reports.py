from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class EventReport:
    """
    Event report model.
    Attributes:
        event_id (str): The ID of the reported event
        id (int): ID of event report
        reason (str|None): Comment made by the user_id in this report
        score (int|None): Content is reported based upon a negative score, where -100 is "most offensive" and 0 is "inoffensive"
        received_ts (int): The timestamp (in milliseconds since the unix epoch) when this report was sent
        canonical_alias (str): The canonical alias of the room. null if the room does not have a canonical alias set.
        room_id (str): The ID of the room in which the event being reported is located
        name (str): The name of the room
        sender (str): This is the ID of the user who sent the original message/event that was reported.
        user_id (str): This is the user who reported the event and wrote the reason
    """

    event_id: str
    id: int
    reason: Optional[str]
    score: Optional[int]
    received_ts: int
    canonical_alias: str
    room_id: str
    name: str
    sender: str
    user_id: str


@dataclass
class EventReports:
    """
    List of Event Reports
    Attributes:
        event_reports (List[EventReport]): List of Event Reports
        next_token (int): Indication for pagination
        total (int): Total number of event reports related to the query
    """

    event_reports: List[EventReport]
    next_token: int
    total: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EventReports":
        return cls(
            next_token=data["next_token"],
            total=data["total"],
            event_reports=[EventReport(**i) for i in data["event_reports"]],
        )
