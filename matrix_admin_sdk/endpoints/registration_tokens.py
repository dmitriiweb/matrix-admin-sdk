from typing import Any, Dict, List, Optional

from matrix_admin_sdk.models.registration_tokens import RegistrationTokensModel

from .endpoint import Endpoint


class MatrixAdminSdkErrorRegistrationTokens(Exception):
    def __init__(self, code: str, error: str, http_status_code: int):
        message = f"{code}: {error} {http_status_code=}"
        super().__init__(message)


class RegistrationTokens(Endpoint):
    """
    This API allows you to manage tokens which can be used to authenticate
    registration requests, as proposed in MSC3231. To use it, you will need to
    enable the registration_requires_token config option, and authenticate by
    providing an access_token for a server admin: see Admin API. Note that this API
    is still experimental; not all clients may support it yet.
    """

    async def list_all_tokens(
        self, valid: Optional[bool] = None
    ) -> List[RegistrationTokensModel]:
        url = self.url("registration_tokens")
        params = {"valid": valid}

        response = await self.admin_client.get(url, params=params)
        res = response.json()
        self._is_error(res, response.status_code)

        result: List[RegistrationTokensModel] = [
            RegistrationTokensModel.from_dict(d) for d in res["registration_tokens"]
        ]
        return result

    async def get_one_token(self, token: str) -> RegistrationTokensModel:
        """
        Get details about a single token. If the request is successful, the response
        body will be a registration token object.
        Args:
            token: The registration token to return details of.

        Returns: RegistrationTokensModel

        """
        url = self.url(f"registration_tokens/{token}")
        response = await self.admin_client.get(url)
        res = response.json()
        self._is_error(res, response.status_code)
        result: RegistrationTokensModel = RegistrationTokensModel.from_dict(res)
        return result

    async def create_token(
        self,
        token: Optional[str] = None,
        uses_allowed: Optional[int] = None,
        expiry_time: Optional[int] = None,
        length: int = 16,
    ) -> RegistrationTokensModel:
        """
        Create a new registration token. If the request is successful, the newly
        created token will be returned as a registration token object in the
        response body.

        Args:
            token: The registration token. A string of no more than 64 characters
                that consists only of characters matched by the regex [A-Za-z0-9._~-].
                Default: None and will be randomly generated on a server.
            uses_allowed: The integer number of times the token can be used to
                complete a registration before it becomes invalid.
                Default: None (unlimited uses).
            expiry_time: The latest time the token is valid. Given as the
                number of milliseconds since 1970-01-01 00:00:00 UTC
                (the start of the Unix epoch)
            length: The length of the token randomly generated if token is
                not specified. Must be between 1 and 64 inclusive. Default: 16

        Returns: RegistrationTokensModel

        """
        if length < 1 or length > 64:
            raise ValueError("length must be between 1 and 64 inclusive")

        url = self.url("registration_tokens/new")
        data = {
            "token": token,
            "uses_allowed": uses_allowed,
            "expiry_time": expiry_time,
            "length": length,
        }
        response = await self.admin_client.post(url, data=data)
        res = response.json()
        self._is_error(res, response.status_code)

        result: RegistrationTokensModel = RegistrationTokensModel.from_dict(res)
        return result

    async def update_token(
        self,
        token: str,
        uses_allowed: Optional[int] = None,
        expiry_time: Optional[int] = None,
    ) -> RegistrationTokensModel:
        """
        Update the number of allowed uses or expiry time of a token. If the
        request is successful, the updated token will be returned as a registration
        token object in the response body.
        Args:
            token: The registration token to update
            uses_allowed: The integer number of times the token can be used to
                complete a registration before it becomes invalid. By setting
                uses_allowed to 0 the token can be easily made invalid without
                deleting it. If None the token will have an unlimited number of uses.
                Default: None (unlimited uses).
            expiry_time: The latest time the token is valid. Given as the number
                of milliseconds since 1970-01-01 00:00:00 UTC (the start of the Unix
                epoch). If null the token will not expire
                Default: None (no expiry)

        Returns: RegistrationTokensModel

        """
        url = self.url(f"registration_tokens/{token}")
        data = {"uses_allowed": uses_allowed, "expiry_time": expiry_time}
        response = await self.admin_client.put(url, data=data)
        res = response.json()
        self._is_error(res, response.status_code)
        result: RegistrationTokensModel = RegistrationTokensModel(**res)
        return result

    async def delete_token(self, token: str) -> Dict[Any, Any]:
        """
        Delete a registration token.
        Args:
            token: The registration token to delete

        Returns: Dict[Any, Any]

        """
        url = self.url(f"registration_tokens/{token}")
        response = await self.admin_client.delete(url, data={})
        res = response.json()
        self._is_error(res, response.status_code)
        return res

    def _is_error(self, res: Dict[str, Any], status_code: int) -> None:
        if "error" not in res:
            return
        message = res["error"]
        code = res["errcode"]
        raise MatrixAdminSdkErrorRegistrationTokens(
            code, message, http_status_code=status_code
        )
