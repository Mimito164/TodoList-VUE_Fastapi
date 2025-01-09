from typing import Optional, List
from pydantic import BaseModel

class TodoItem (BaseModel):
    id: Optional[str]
    description: Optional[str]
    subTodoItems: List['TodoItem']
    status: bool
