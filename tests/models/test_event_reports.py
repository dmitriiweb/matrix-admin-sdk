from matrix_admin_sdk.models.event_reports import EventDetails, EventReports


event_reports = {
    "event_reports": [
        {
            "event_id": "$bNUFCwGzWca1meCGkjp-zwslF-GfVcXukvRLI1_FaVY",
            "id": 2,
            "reason": "foo",
            "score": -100,
            "received_ts": 1570897107409,
            "canonical_alias": "#alias1:matrix.org",
            "room_id": "!ERAgBpSOcCCuTJqQPk:matrix.org",
            "name": "Matrix HQ",
            "sender": "@foobar:matrix.org",
            "user_id": "@foo:matrix.org",
        },
        {
            "event_id": "$3IcdZsDaN_En-S1DF4EMCy3v4gNRKeOJs8W5qTOKj4I",
            "id": 3,
            "reason": "bar",
            "score": -100,
            "received_ts": 1598889612059,
            "canonical_alias": "#alias2:matrix.org",
            "room_id": "!eGvUQuTCkHGVwNMOjv:matrix.org",
            "name": "Your room name here",
            "sender": "@foobar:matrix.org",
            "user_id": "@bar:matrix.org",
        },
    ],
    "next_token": 2,
    "total": 4,
}

event_details = {
    "event_id": "$bNUFCwGzWca1meCGkjp-zwslF-GfVcXukvRLI1_FaVY",
    "event_json": {
        "auth_events": [
            "$YK4arsKKcc0LRoe700pS8DSjOvUT4NDv0HfInlMFw2M",
            "$oggsNXxzPFRE3y53SUNd7nsj69-QzKv03a1RucHu-ws",
        ],
        "content": {
            "body": "matrix.org: This Week in Matrix",
            "format": "org.matrix.custom.html",
            "formatted_body": '<strong>matrix.org</strong>:<br><a href="https://matrix.org/blog/"><strong>This Week in Matrix</strong></a>',
            "msgtype": "m.notice",
        },
        "depth": 546,
        "hashes": {"sha256": "xK1//xnmvHJIOvbgXlkI8eEqdvoMmihVDJ9J4SNlsAw"},
        "origin": "matrix.org",
        "origin_server_ts": 1592291711430,
        "prev_events": ["$YK4arsKKcc0LRoe700pS8DSjOvUT4NDv0HfInlMFw2M"],
        "prev_state": [],
        "room_id": "!ERAgBpSOcCCuTJqQPk:matrix.org",
        "sender": "@foobar:matrix.org",
        "signatures": {
            "matrix.org": {
                "ed25519:a_JaEG": "cs+OUKW/iHx5pEidbWxh0UiNNHwe46Ai9LwNz+Ah16aWDNszVIe2gaAcVZfvNsBhakQTew51tlKmL2kspXk/Dg"
            }
        },
        "type": "m.room.message",
        "unsigned": {"age_ts": 1592291711430},
    },
    "id": "<report_id>",
    "reason": "foo",
    "score": -100,
    "received_ts": 1570897107409,
    "canonical_alias": "#alias1:matrix.org",
    "room_id": "!ERAgBpSOcCCuTJqQPk:matrix.org",
    "name": "Matrix HQ",
    "sender": "@foobar:matrix.org",
    "user_id": "@foo:matrix.org",
}


def test_event_reports():
    er = EventReports.from_dict(event_reports)
    assert er.total == 4
    assert er.event_reports[0].id == 2


def test_event_details():
    ed = EventDetails.from_dict(event_details)

    assert ed.event_id == "$bNUFCwGzWca1meCGkjp-zwslF-GfVcXukvRLI1_FaVY"
    assert ed.reason == "foo"
    assert isinstance(ed.event_json.auth_events, list)
    assert ed.event_json.content.msgtype == "m.notice"
    assert ed.event_json.origin == "matrix.org"
    assert isinstance(ed.event_json.prev_events, list)
    assert isinstance(ed.event_json.signatures, dict)
