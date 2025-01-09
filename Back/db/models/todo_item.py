from typing import Optional, List
from pydantic import BaseModel, Field

class TodoItem (BaseModel):
    id: Optional[str] =  Field(alias="_id",default=None)
    description: Optional[str] = Field(default="")
    subTodoItems: Optional[List['TodoItem']] = Field(default=[])
    status: bool = Field(default=None)
