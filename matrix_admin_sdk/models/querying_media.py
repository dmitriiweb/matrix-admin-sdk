from dataclasses import dataclass
from typing import List


@dataclass
class QueryingMediaModel:
    """
    Querying media model.
    Attributes:
        local (list[str]):
        remote (list[str]):
    """

    local: List[str]
    remote: List[str]
