from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Hello Stack API")

class Item(BaseModel):
    id: int
    name: str

# In-memory "database"
ITEMS = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return ITEMS

@app.post("/items", status_code=201)
def create_item(item: Item):
    ITEMS.append(item)
    return item
