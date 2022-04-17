from matrix_admin_sdk.models.user import CurrentSessionsModel


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
