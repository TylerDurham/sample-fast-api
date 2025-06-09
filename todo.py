from enum import IntEnum
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

api = FastAPI()


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel):
    name: str = Field(
        ..., min_length=3, max_length=512, description="The name of the todo."
    )
    description: str = Field(..., description="The description of the todo.")
    priority: Priority = Field(
        default=Priority.LOW, description="The priority of the todo."
    )


class Todo(TodoBase):
    id: int = Field(..., description="The unique id of the todo.")


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    name: Optional[str] = Field(
        min_length=3, max_length=512, description="The name of the todo."
    )
    description: Optional[str] = Field(description="The description of the todo.")
    priority: Optional[Priority] = Field(
        default=Priority.LOW, description="The priority of the todo."
    )


ALL_TODOs: List[Todo] = [
    Todo(id=1, name="Task 1", description="Do task 1.", priority=Priority.LOW),
    Todo(
        id=2,
        name="Task 2",
        description="Do task 2.",
        priority=Priority.MEDIUM,
    ),
    Todo(id=3, name="Task 3", description="Do task 3.", priority=Priority.HIGH),
    Todo(id=4, name="Task 4", description="Do task 4.", priority=Priority.LOW),
    Todo(
        id=5,
        name="Task 5",
        description="Do task 5.",
        priority=Priority.MEDIUM,
    ),
]


@api.get("/todos", response_model=List[Todo])
async def get_all_todos(first_n: int = 0) -> List[Todo]:
    "Get all todos from the database."
    if first_n > 0:
        return ALL_TODOs[:first_n]
    else:
        return ALL_TODOs


@api.get("/todos/{id}", response_model=Todo)
async def get_todo(id: int):
    """Gets the specified todo from the database."""
    for todo in ALL_TODOs:
        if todo.id == id:
            return todo

    raise HTTPException(status_code=404, detail=f"Todo {id} not found in the database.")


@api.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    """Create a new todo in the database."""
    new_id = max(todo.id for todo in ALL_TODOs) + 1

    new_todo = Todo(id=new_id, name=todo.name, description=todo.description)

    ALL_TODOs.append(new_todo)

    return new_todo


@api.put("/todos", response_model=Todo)
async def update_todo(id: int, updated_todo: TodoUpdate):
    """Update an existing todo in the database."""
    for todo in ALL_TODOs:
        if todo.id == id:
            if todo.name is not None:
                todo.name = updated_todo.name
            if todo.description is not None:
                todo.description = updated_todo.description
            if todo.priority is not None:
                todo.priority = updated_todo.priority

            return todo

    raise HTTPException(status_code=404, detail=f"Todo {id} not found in the database.")


@api.delete("/todos/{id}", response_model=Todo)
async def delete_todo(id: int):
    """Delete the specified todo from the database."""
    for index, todo in enumerate(ALL_TODOs):
        if todo.id == id:
            deleted_todo = ALL_TODOs.pop(index)
            return deleted_todo

    raise HTTPException(status_code=404, detail=f"Todo {id} not found in the database.")
