from fastapi import FastAPI, HTTPException

api = FastAPI()

ALL_TODOs = [
    {"id": 1, "title": "Task 1", "description": "Do task 1."},
    {"id": 2, "title": "Task 2", "description": "Do task 2."},
    {"id": 3, "title": "Task 3", "description": "Do task 3."},
    {"id": 4, "title": "Task 4", "description": "Do task 4."},
    {"id": 5, "title": "Task 5", "description": "Do task 5."},
]


@api.get("/")
async def index():
    return {"result": "Navigate to /todos"}


@api.get("/todos")
async def get_all_todos(first_n: int = 0):
    if first_n > 0:
        return ALL_TODOs[:first_n]
    else:
        return ALL_TODOs


@api.get("/todos/{id}")
async def get_todo(id: int):
    for todo in ALL_TODOs:
        if todo["id"] == id:
            return {"result": todo}
    raise HTTPException(status_code=404, detail=f"Todo {id} not found in the database.")


@api.post("/todos")
def create_todo(todo: dict):
    new_id = max(todo["id"] for todo in ALL_TODOs) + 1

    new_todo = {
        "id": new_id,
        "title": todo["title"],
        "description": todo["description"],
    }

    ALL_TODOs.append(new_todo)

    return new_todo


@api.put("/todos")
async def update_todo(id: int, updated_todo: dict):
    for todo in ALL_TODOs:
        if todo["id"] == id:
            todo["title"] = updated_todo["title"]
            todo["description"] = updated_todo["description"]
            return todo

    raise HTTPException(status_code=404, detail=f"Todo {id} not found in the database.")


@api.delete("/todos/{id}")
async def delete_todo(id: int):
    for index, todo in enumerate(ALL_TODOs):
        if todo["id"] == id:
            deleted_todo = ALL_TODOs.pop(index)
            return deleted_todo

    raise HTTPException(status_code=404, detail=f"Todo {id} not found in the database.")
