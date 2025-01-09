from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from pyobjectID import MongoObjectId

class User(BaseModel):
    id: Optional[MongoObjectId] = Field(alias="_id",default=None)
    todolistIDs: List[MongoObjectId]
    wallet: str

    model_config = ConfigDict(populate_by_name=True,arbitrary_types_allowed=True)

