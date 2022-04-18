from matrix_admin_sdk.models.user import CurrentSessionsModel, PushersModel


PUSHERS = {
    "pushers": [
        {
            "app_display_name": "HTTP Push Notifications",
            "app_id": "m.http",
            "data": {"url": "example.com"},
            "device_display_name": "pushy push",
            "kind": "http",
            "lang": "None",
            "profile_tag": "",
            "pushkey": "a@example.com",
        }
    ],
    "total": 1,
}

CURRENT_SESSIONS = {
    "user_id": "<user_id>",
    "devices": {
        "": {
            "sessions": [
                {
                    "connections": [
                        {
                            "ip": "1.2.3.4",
                            "last_seen": 1417222374433,
                            "user_agent": "Mozilla/5.0 ...",
                        },
                        {
                            "ip": "1.2.3.10",
                            "last_seen": 1417222374500,
                            "user_agent": "Dalvik/2.1.0 ...",
                        },
                    ]
                }
            ]
        }
    },
}


def test_query_current_session():
    cs = CurrentSessionsModel.from_dict(CURRENT_SESSIONS)

    assert cs.user_id == CURRENT_SESSIONS["user_id"]
    assert isinstance(cs.devices, dict)
    assert cs.devices[""][0].ip == "1.2.3.4"


def test_pushers_model():
    m = PushersModel.from_dict(PUSHERS)
    assert m.total == 1
    assert m.pushers[0].app_display_name == "HTTP Push Notifications"
    assert m.pushers[0].data.url == "example.com"
