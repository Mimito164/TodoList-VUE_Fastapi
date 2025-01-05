from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    wallet: str
