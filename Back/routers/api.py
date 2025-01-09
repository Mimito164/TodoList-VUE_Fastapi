from fastapi import APIRouter, HTTPException, status, Response
from ..db.models.user import User
from ..db.models.todo_list import TodoList, CreateTodoList
from ..db.models.todo_item import TodoItem
from ..db.client import client, users, todolists
from bson import ObjectId

router = APIRouter(
    prefix="/api"
)

# users

@router.post("/user/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User, response: Response):
    founded = users.find_one({"wallet": user.wallet})
    if founded is not None:
        response.status_code = status.HTTP_200_OK

        return User(**founded)
  
    new_user = users.insert_one( user.model_dump(by_alias=True,exclude={"id"}) )
    
    created_user = users.find_one({"_id": new_user.inserted_id})

    return User(**created_user)

@router.get("/user/{id}/")
async def find_user(id:str) ->  User:
    try:
        user_found = users.find_one({"_id": ObjectId(id)})
        return User(**user_found)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")

@router.get("/users/")
async def find_users() -> list[User]:
    
    return [User(**user) for user in users.find() ]

# @router.delete("/user/{id}")
# async def delete_user(id) -> User:
#     return "hola"


# todolists
@router.get("/todolists/{user_id}/", status_code=status.HTTP_200_OK)
async def get_todolists_from_user(user_id:str) :
    try:
        user_found = users.find_one({"_id": ObjectId(user_id)})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
    user = User(**user_found)
    todolist_object_ids = [ObjectId(id) for id in user.todolistIDs]
    founded_todolists = todolists.find({
        "_id": {
            "$in":todolist_object_ids
        }
    })
    return [TodoList(**todolist) for todolist in founded_todolists]

@router.get("/todolists/{user_id}/{list_id}/", response_model=TodoList, status_code=status.HTTP_200_OK)
async def get_todolist(user_id:str, id:str):
    try:
        users.find_one({"_id": ObjectId(user_id)})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
    try:
        todolist_found = todolists.find_one({"_id": ObjectId(id)})
        return TodoList(**todolist_found)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La TodoList no existe")

@router.post("/todolists/", response_model=TodoList, status_code=status.HTTP_201_CREATED)
async def create_todolist(create_todoList:CreateTodoList):
    try:
        users.find_one({"_id": ObjectId(create_todoList.user_id)})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")

    
    todolist = TodoList(name=create_todoList.todolist_name)
    new_todolist = todolists.insert_one(todolist.model_dump(by_alias=True, exclude={"id"})) 

    users.update(
        {"_id":ObjectId(create_todoList.user_id)},
        {
            '$push': {"todolistIDs":new_todolist.inserted_id}
        }
    )
    
    created_todolist = todolists.find_one({"_id":ObjectId(new_todolist.inserted_id)})
    return TodoList(**created_todolist)