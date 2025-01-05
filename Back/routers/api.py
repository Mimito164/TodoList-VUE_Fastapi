from fastapi import APIRouter, HTTPException, status
from ..db.models import models
from ..db.schemas import schemas
from ..db.client import client
from bson import ObjectId

router = APIRouter(
    prefix="/api"
)

@router.get("/")
async def root():
    return {"msg":"xd"}

@router.get("/v1/health")
async def health_check():
    return {"status": "healthy"}

# users

@router.post("/user", response_model=models.User, status_code=status.HTTP_201_CREATED)
async def create_user(user: models.User):
    user_dict = dict(user)
  
    del user_dict["id"]

    id = client.users.insert_one(user_dict).inserted_id

    new_user = schemas.user_schema(client.users.find_one({"_id": id}))

    return models.User(**new_user)



@router.get("/user/{id}")
async def find_user(id:str) ->  models.User:

    try:
        user_found = schemas.user_schema(client.users.find_one({"_id": ObjectId(id)}))
        return models.User(**user_found)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
        
@router.get("/users")
async def find_users() -> list[models.User]:
    
    return schemas.users_schema (client.users.find())

@router.delete("/user/{id}")
async def delete_user(id) -> models.User:
    return "hola"
