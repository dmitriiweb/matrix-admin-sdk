from matrix_admin_sdk.models.v2.users import UserDetailsModel


USER_DETAILS = {
    "name": "@user:example.com",
    "displayname": "User",
    "threepids": [
        {
            "medium": "email",
            "address": "<user_mail_1>",
            "added_at": 1586458409743,
            "validated_at": 1586458409743,
        },
        {
            "medium": "email",
            "address": "<user_mail_2>",
            "added_at": 1586458409743,
            "validated_at": 1586458409743,
        },
    ],
    "avatar_url": "<avatar_url>",
    "is_guest": 0,
    "admin": 0,
    "deactivated": 0,
    "shadow_banned": 0,
    "creation_ts": 1560432506,
    "appservice_id": None,
    "consent_server_notice_sent": None,
    "consent_version": None,
    "external_ids": [
        {"auth_provider": "<provider1>", "external_id": "<user_id_provider_1>"},
        {"auth_provider": "<provider2>", "external_id": "<user_id_provider_2>"},
    ],
    "user_type": None,
}


def test_user_details_from_dict():
    m = UserDetailsModel.from_dict(USER_DETAILS)
    assert m.name == USER_DETAILS["name"]
    assert m.threepids[0].address == USER_DETAILS["threepids"][0]["address"]
    assert (
        m.external_ids[0].auth_provider
        == USER_DETAILS["external_ids"][0]["auth_provider"]
    )
