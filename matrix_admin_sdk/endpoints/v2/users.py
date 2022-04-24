from enum import Enum
from typing import Optional

from matrix_admin_sdk.endpoints import RequestMethods
from matrix_admin_sdk.models.v2.users import UsersModel

from .endpoint import Endpoint


class OrderBy(Enum):
    """
    Enum for order by options
    Attributes:
        NAME (str): Users are ordered alphabetically by name. This is the default.
        IS_GUEST (str): Users are ordered by is_guest status.
        ADMIN (str): Users are ordered by admin status.
        USER_TYPE (str): Users are ordered alphabetically by user_type.
        DEACTIVATED (str): Users are ordered by deactivated status.
        SHADOW_BANNED (str): Users are ordered by shadow_banned status.
        DISPLAYNAME (str): Users are ordered alphabetically by displayname
        AVATAR_URL (str): Users are ordered alphabetically by avatar URL.
        CREATION_TS (str): Users are ordered by when the users was created in ms.
    """

    NAME = "name"
    IS_GUEST = "is_guest"
    ADMIN = "admin"
    USER_TYPE = "user_type"
    DEACTIVATED = "deactivated"
    SHADOW_BANNED = "shadow_banned"
    DISPLAYNAME = "displayname"
    AVATAR_URL = "avatar_url"
    CREATION_TS = "creation_ts"


class Users(Endpoint):
    async def get_all(
        self,
        user_id: Optional[str] = None,
        name: Optional[str] = None,
        guests: bool = True,
        deactivated: bool = False,
        limit: int = 100,
        from_: int = 0,
        order_by: Optional[OrderBy] = None,
        dir_: str = "f",
    ) -> UsersModel:
        order_by = OrderBy.NAME if order_by is None else order_by

        url = self.url("users")
        params = {
            "user_id": user_id,
            "name": name,
            "guests": guests,
            "deactivated": deactivated,
            "limit": limit,
            "from": from_,
            "order_by": order_by.value,
            "dir": dir_,
        }
        result = await self.request(RequestMethods.GET, url, params=params)
        res: UsersModel = UsersModel.from_dict(result)
        return res
