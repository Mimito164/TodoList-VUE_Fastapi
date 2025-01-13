from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from pyobjectID import MongoObjectId

from .todo_item import TodoItem

class TodoList(BaseModel):
    id: Optional[MongoObjectId] = Field(alias="_id",default=None)
    name: Optional[str] = Field(default=None)
    todoItems: Optional[List[TodoItem]] =  Field(default=[])

    model_config = ConfigDict(populate_by_name=True,arbitrary_types_allowed=True)

class CreateTodoList(BaseModel):
    todolist_name: str
    user_id: MongoObjectId

class UpdateTodoList(BaseModel):
    user_id: str
    todolist_id: str
    todolist_name: Optional[str] = Field(default="")
    todo_item: Optional[TodoItem] = Field(default=None)