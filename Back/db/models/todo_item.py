from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field
from pyobjectID import MongoObjectId


class TodoItem (BaseModel):
    id: Optional[MongoObjectId] =  Field(alias="_id",default=None)
    description: Optional[str] = Field(default="")
    subTodoItems: Optional[List['TodoItem']] = Field(default=[])
    done: Optional[bool] = Field(default=False)

    model_config = ConfigDict(populate_by_name=True,arbitrary_types_allowed=True)

class UpdateTodoItem(BaseModel):
    list_id:str
    item_id:str
    description: Optional[str] = Field(default="")


# --------------------------------------------------
class AddSubTodoItem(BaseModel):
    list_id:str
    item_id:str
    description:str = Field(default="")

class UpdateSubTodoItem(BaseModel):
    # list_id:str
    item_id:str
    subitem_id:str
    description: Optional[str] = Field(default="")