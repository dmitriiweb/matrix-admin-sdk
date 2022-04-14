from matrix_admin_sdk.models.rooms import RoomsModel


ROOMS = {
    "rooms": [
        {
            "room_id": "!OGEhHVWSdvArJzumhm:matrix.org",
            "name": "Matrix HQ",
            "canonical_alias": "#matrix:matrix.org",
            "joined_members": 8326,
            "joined_local_members": 2,
            "version": "1",
            "creator": "@foo:matrix.org",
            "encryption": None,
            "federatable": True,
            "public": True,
            "join_rules": "invite",
            "guest_access": None,
            "history_visibility": "shared",
            "state_events": 93534,
        },
        {
            "room_id": "!xYvNcQPhnkrdUmYczI:matrix.org",
            "name": "This Week In Matrix (TWIM)",
            "canonical_alias": "#twim:matrix.org",
            "joined_members": 314,
            "joined_local_members": 20,
            "version": "4",
            "creator": "@foo:matrix.org",
            "encryption": "m.megolm.v1.aes-sha2",
            "federatable": True,
            "public": False,
            "join_rules": "invite",
            "guest_access": None,
            "history_visibility": "shared",
            "state_events": 8345,
        },
    ],
    "offset": 0,
    "total_rooms": 10,
}


def test_from_dict():
    rooms = RoomsModel.from_dict(ROOMS)
    assert rooms.rooms[0].room_id == "!OGEhHVWSdvArJzumhm:matrix.org"
    assert rooms.rooms[0].name == "Matrix HQ"
    assert rooms.total_rooms == 10
