import os
import sys

# Add the project root (hello-stack) to sys.path so "app" can be imported
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from fastapi.testclient import TestClient
from app.main import app, ITEMS


client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_create_item_and_list():
    # reset in-memory DB
    ITEMS.clear()

    new_item = {"id": 1, "name": "Test Item"}
    resp = client.post("/items", json=new_item)
    assert resp.status_code == 201
    assert resp.json() == new_item

    resp_list = client.get("/items")
    assert resp_list.status_code == 200
    assert resp_list.json() == [new_item]


def test_get_item_by_id():
    ITEMS.clear()

    item_one = {"id": 1, "name": "First"}
    item_two = {"id": 2, "name": "Second"}
    client.post("/items", json=item_one)
    client.post("/items", json=item_two)

    resp = client.get("/items/2")
    assert resp.status_code == 200
    assert resp.json() == item_two


def test_get_item_not_found():
    ITEMS.clear()

    resp = client.get("/items/999")
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Item not found"}
