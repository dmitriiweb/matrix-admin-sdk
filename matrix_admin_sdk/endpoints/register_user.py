from matrix_admin_sdk.models.register_user import NewUserModel

from .endpoint import Endpoint


class RegisterUsers(Endpoint):
    """
    This API allows for the creation of users in an administrative and non-interactive
    way. This is generally used for bootstrapping a Synapse instance with
    administrator accounts.
    """

    async def get_nonce(self) -> str:
        """
        To authenticate yourself to the server, you will need both the shared secret
        (registration_shared_secret in the homeserver configuration),
        and a one-time nonce. If the registration shared secret is not configured,
        this API is not enabled.

        To fetch the nonce, you need to request one from the API
        """
        url = self.url("register")
        response = await self.admin_client.get(url)
        nonce: str = response.json()["nonce"]
        return nonce

    async def register(
        self,
        nonce: str,
        username: str,
        displayname: str,
        password: str,
        admin: bool,
        mac: str,
    ) -> NewUserModel:
        """
        Register a new user.
        Args:
            nonce: nonce returned by get_nonce
            username: user's name
            displayname: user's display name
            password: user's password
            admin: is user an admin
            mac: please use utils.generate_mac to generate this

        Returns: new user model

        """
        url = self.url("register")
        data = {
            "nonce": nonce,
            "username": username,
            "displayname": displayname,
            "password": password,
            "admin": admin,
            "mac": mac,
        }
        response = await self.admin_client.post(url, data=data)
        res: NewUserModel = NewUserModel.from_dict(response.json())
        return res
