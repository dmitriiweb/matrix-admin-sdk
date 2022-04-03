from matrix_admin_sdk.models.event_reports import EventReports


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


def test_event_reports():
    er = EventReports.from_dict(event_reports)
    assert er.total == 4
    assert er.event_reports[0].id == 2
