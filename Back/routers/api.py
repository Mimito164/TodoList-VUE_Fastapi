from fastapi import APIRouter, HTTPException, status, Response
from ..db.models.user import User
from ..db.models.todo_list import TodoList
from ..db.models.todo_item import TodoItem
from ..db.schemas.user import user_schema, users_schema
from ..db.schemas.todo_list import todolist_schema
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

@router.post("/user", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User, response: Response):
    founded = client.users.find_one({"wallet": user.wallet})
    print(founded)
    if founded is not None:
        response.status_code = status.HTTP_200_OK
        return User(**user_schema(founded))
    print("user", user)
    user_dict = dict(user)
  
    del user_dict["id"] 
    id = client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(client.users.find_one({"_id": id}))

    return User(**new_user)

@router.get("/user/{id}")
async def find_user(id:str) ->  User:
    print("id",id)
    print(client.users.find_one({"_id": ObjectId(id)}))
    try:
        user_found = user_schema(client.users.find_one({"_id": ObjectId(id)}))
        return User(**user_found)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
        
@router.get("/users")
async def find_users() -> list[User]:
    
    return users_schema(client.users.find())

@router.delete("/user/{id}")
async def delete_user(id) -> User:
    return "hola"


# todolists
@router.get("/todolist/{id}/", response_model=TodoList, status_code=status.HTTP_200_OK)
async def get_todolist(id:str):
    try:
        todolist_fount = todolist_schema(client.todolists.find_one({"_id": ObjectId(id)}))
        return TodoList(**todolist_fount)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La TodoList no existe")

@router.post("/todolist/{user_ID}/", response_model=TodoList, status_code=status.HTTP_201_CREATED)
async def create_todolist(user_ID:str, todolist:TodoList):
    todolist_dict = dict(todolist)
    del todolist_dict["id"]
    todolist_id = client.todolists.insert_one(todolist_dict).inserted_id
    client.users.update(
        {"_id":ObjectId(user_ID)},
        {
            '$push': {"todolistIDs":todolist_id}
        }
    )
    new_user = todolist_schema(client.todolists.find_one({"_id":ObjectId(todolist_id)}))
    return TodoList(**new_user)

