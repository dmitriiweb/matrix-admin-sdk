from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from matrix_admin_sdk.models.base_model import BaseModel


@dataclass
class UserModel(BaseModel):
    """
    User model
    Attributes:
        name (str): Fully-qualified user ID (ex. @user:server.com).
        is_guest (bool): Status if that user is a guest account.
        admin (bool): Status if that user is an admin account.
        deactivated (bool): Status if that user has been marked as deactivated.
        shadow_banned (bool): Status if that user has been marked as shadow banned.
        displayname (str): The user's display name if they have set one.
        creation_ts (int): The user's creation timestamp in ms.
        avatar_url (str|None): he user's avatar URL if they have set one
        user_type (str|None): Type of the user. Normal users are type None.
            This allows user type specific behaviour. There are also types support and bot
    """

    name: str
    is_guest: bool
    admin: bool
    deactivated: bool
    shadow_banned: bool
    displayname: str
    creation_ts: int
    avatar_url: Optional[str] = None
    user_type: Optional[str] = None


@dataclass
class UsersModel(BaseModel):
    """
    List of users
    Attributes:
        users (list[UserModel]): List of users
        total (int): total number of users
        next_token (str|None): next token

    """

    users: List[UserModel]
    total: int
    next_token: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        users = [UserModel.from_dict(i) for i in data["users"]]
        return cls(users=users, total=data["total"], next_token=data.get("next_token"))
