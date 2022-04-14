from dataclasses import dataclass


@dataclass
class NewUserModel:
    access_token: str
    user_id: str
    home_server: str
    device_id: str
