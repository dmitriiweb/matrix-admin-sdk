from matrix_admin_sdk.models.background_updates import StatusModel


def test_status_model():
    response = {
        "enabled": True,
        "current_updates": {
            "<db_name>": {
                "name": "<background_update_name>",
                "total_item_count": 50,
                "total_duration_ms": 10000.0,
                "average_items_per_ms": 2.2,
            },
        },
    }
    model = StatusModel.from_dict(response)
    assert model.enabled is True
    assert model.current_updates[0].name == "<background_update_name>"
