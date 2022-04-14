from dataclasses import dataclass
from typing import List


@dataclass
class DeleteLocalMediaModel:
    """
    DeleteLocalMedia class
    Attributes:
        deleted_media (list[str]): List of deleted media_id
        total (int): Total number of deleted media_id
    """

    deleted_media: List[str]
    total: int
