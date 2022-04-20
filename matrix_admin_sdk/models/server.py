from dataclasses import dataclass

from .base_model import BaseModel


@dataclass
class ServerVersionModel(BaseModel):
    """
    Server version model.
    Attributes:
        server_version (str): Synapse version
        python_version (str): Python version
    """

    server_version: str
    python_version: str
