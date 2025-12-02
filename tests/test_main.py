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
