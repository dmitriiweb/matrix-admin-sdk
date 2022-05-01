from matrix_admin_sdk.endpoints import RequestMethods
from matrix_admin_sdk.models.v2.user_devices import UserDevicesModel

from .endpoint import Endpoint


class UserDevices(Endpoint):
    def __int__(self, user_id: str, **kwargs):
        """
        Initialize UserDevices endpoint
        Args:
            user_id: fully-qualified user id: for example, @user:server.com
            **kwargs: keyword arguments to pass to Endpoint

        Returns: None

        """
        self.user_id = user_id
        super().__init__(**kwargs)

    async def get_all(self) -> UserDevicesModel:
        """
        Gets information about all devices for a specific user_id.

        Returns: UserDevicesModel

        """
        url = self.url(f"users/{self.user_id}/devices")
        result = await self.request(RequestMethods.GET, url)
        res: UserDevicesModel = UserDevicesModel.from_dict(result)
        return res
