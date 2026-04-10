from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_item_with_valid_user_id():
    response = client.get("/items/?user_id=validuser")
    assert response.status_code == 200
    assert response.json() == {"user_id": "validuser"}


def test_read_item_with_empty_user_id():
    response = client.get("/items/?user_id=")
    assert response.status_code == 400
    assert response.json() == {"detail": "user_id cannot be empty"}


def test_read_item_with_whitespace_user_id():
    response = client.get("/items/?user_id= ")
    assert response.status_code == 400
    assert response.json() == {"detail": "user_id cannot be empty"}
