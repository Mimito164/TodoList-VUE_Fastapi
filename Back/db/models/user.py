from bson import ObjectId
from pydantic import BaseModel, ValidationError, validator
from typing import Optional, List, Annotated
from pydantic.json_schema import JsonSchemaValue
from pydantic.fields import Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field: Field = None):
        if v in (None, ""):  # Allow None or empty string
            return None
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return cls(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: JsonSchemaValue) -> JsonSchemaValue:
        schema.update(type="string")
        return schema

  

class User(BaseModel):
    id: Optional[PyObjectId]
    todolistIDs: List[PyObjectId]
    wallet: str
    class Config:
        json_encoders = {
            ObjectId: str,
        }
