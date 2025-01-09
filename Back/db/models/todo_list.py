from pydantic import BaseModel
from typing import List, Optional

from .todo_item import TodoItem

class TodoList(BaseModel):
    id: Optional[str]
    name: str
    todoItems: List[TodoItem]

