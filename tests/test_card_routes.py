def test_create_card_too_long(client):
    board_response = client.post("/boards", json={
        "title": "Board",
        "owner": "Test"
    })
    board_id = board_response.get_json()["id"]

    response = client.post(f"/boards/{board_id}/cards", json={
        "message": "x" * 100
    })

    assert response.status_code == 400
    assert "Invalid" in response.get_json()["details"]
