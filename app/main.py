from fastapi import FastAPI, HTTPException
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

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in ITEMS:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
