from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


fake_items_db = [
    {"id": 1, "item_name": "Foo"},
    {"id": 2, "item_name": "Bar"},
    {"id": 3, "item_name": "Baz"},
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{id}")
async def get_item(id: int):
    found = next((item for item in fake_items_db if item["id"] == id), None)

    if found:
        return found
    else:
        raise HTTPException(status_code=404, detail=f"Item {id} not found.")
