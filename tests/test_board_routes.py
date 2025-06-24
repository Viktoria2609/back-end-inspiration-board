def test_create_board_success(client):
    response = client.post("/boards", json={
        "title": "My Test Board",
        "owner": "Renata"
    })
    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data["title"] == "My Test Board"
    assert response_data["owner"] == "Renata"


def test_create_board_missing_title(client):
    response = client.post("/boards", json={
        "owner": "Renata"
    })
    assert response.status_code == 400
    assert "details" in response.get_json()
