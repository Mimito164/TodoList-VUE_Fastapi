from fastapi import APIRouter, HTTPException, status, Response
from db.models.user import User
from db.models.todo_list import TodoList, CreateTodoList, UpdateTodoList
from db.models.todo_item import TodoItem, UpdateTodoItem, AddSubTodoItem, UpdateSubTodoItem
from db.client import users, todolists
from bson import ObjectId

router = APIRouter(
    prefix="/api"
)

#########
# users #
#########

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
    user_found = find_user_query(id)
    return User(**user_found)

@router.get("/users/")
async def find_users() -> list[User]:
    
    return [User(**user) for user in users.find() ]

# @router.delete("/user/{id}")
# async def delete_user(id) -> User:
#     return "hola"

#############
# todolists #
#############

@router.get("/todolists/{user_id}/", status_code=status.HTTP_200_OK)
async def get_todolists_from_user(user_id:str) :
    user_found = find_user_query(user_id)
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
    find_user_query(user_id)
    try:
        todolist_found = todolists.find_one({"_id": ObjectId(id)})
        return TodoList(**todolist_found)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La TodoList no existe")

@router.post("/todolists/", response_model=TodoList, status_code=status.HTTP_201_CREATED)
async def create_todolist(create_todoList:CreateTodoList):
    find_user_query(create_todoList.user_id)
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

@router.delete("/todolists/{user_id}/{todolist_id}/",status_code=status.HTTP_200_OK)
async def delete_todolist(user_id:str, todolist_id:str):
    find_user_query(user_id)
    users.update(
        {"_id":ObjectId(user_id)},
        {"$pull": {
            "todolistIDs": ObjectId(todolist_id)
        }}
    )
    todolists.find_one_and_delete({"_id":ObjectId(todolist_id)})

# update or add todoitem
@router.put("/todolists/")
async def update_todolist(updateTodoList:UpdateTodoList):
    x = find_user_query(updateTodoList.user_id)
    try:
        if(updateTodoList.todolist_name != ""):
            todolists.find_one_and_update(
                {"_id":ObjectId(updateTodoList.todolist_id)},
                {"$set": {"name":updateTodoList.todolist_name}}
            )
            
            updated_todolist = todolists.find_one({"_id": ObjectId(updateTodoList.todolist_id)})
            
            return TodoList(**updated_todolist )
        if(updateTodoList.todo_item != None):
            new_todoitem_dict = updateTodoList.todo_item.model_dump(by_alias=True,exclude={"id"})
            new_todoitem_dict["_id"] = ObjectId()
            todolists.find_one_and_update(
                {"_id":ObjectId(updateTodoList.todolist_id)},
                {"$push": {"todoItems": new_todoitem_dict}}
            )

            updated_todoitems_list = todolists.find_one({
                "todoItems": {"$elemMatch": new_todoitem_dict}
                })
            

            created_todoitem_index =  updated_todoitems_list["todoItems"].index(new_todoitem_dict)
            created_todoitem = updated_todoitems_list["todoItems"][created_todoitem_index]
            return TodoItem(**created_todoitem )
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The todolists does not exists")

#############
# todoitems #
#############

@router.delete("/todolists/todoitems/{user_id}/{todolist_id}/{todoitem_id}/")
async def remove_todoitem(user_id:str,todolist_id:str,todoitem_id:str):
    find_user_query(user_id)
    print("todobien")
    todolists.update({
        "_id":ObjectId(todolist_id)
    },{
        "$pull": {"todoItems": {"_id":ObjectId(todoitem_id)}}
    })

@router.put("/todolists/todoitems/done/")
async def toggle_todoitem_done(updateTodoItem:UpdateTodoItem):

    target_todolist = todolists.find_one({
        "_id": ObjectId(updateTodoItem.list_id),
        "todoItems._id": ObjectId(updateTodoItem.item_id)
    },
    {
        "todoItems.$":1
    })
    
    if not target_todolist or "todoItems" not in target_todolist :
        raise HTTPException(status_code=404, detail="TodoItem no encontrado.")

    current_done = target_todolist["todoItems"][0]["done"]
    new_done = not current_done

    todolists.find_one_and_update(
    {
        "_id": ObjectId(updateTodoItem.list_id),
        "todoItems._id": ObjectId(updateTodoItem.item_id)
    },
    {
        "$set": {"todoItems.$.done": new_done}
    })

    updated_todolist = todolists.find_one({
        "_id": ObjectId(updateTodoItem.list_id),
        "todoItems._id": ObjectId(updateTodoItem.item_id)
    },
    {
        "todoItems.$":1
    })

    updated_todoItem = updated_todolist["todoItems"][0]
    print(TodoItem(**updated_todoItem))
    return TodoItem(**updated_todoItem)

@router.put("/todolists/todoitems/rename/")
async def rename_todoitem(updateTodoItem:UpdateTodoItem):
    todolists.find_one_and_update({
        "_id":ObjectId(updateTodoItem.list_id),
        "todoItems._id": ObjectId(updateTodoItem.item_id)
    },{
        "$set":{"todoItems.$.description":updateTodoItem.description}
    })

@router.delete("todolists/todoitems/{list_id}/{item_id}/")
async def delete_todoitem(list_id, item_id):
    todolists.find_one_and_update({
        "_id":ObjectId(list_id),
        "todoItems._id":ObjectId(item_id)
    },{
        "$pull": {"todoItems._id":ObjectId(item_id)}
    })


############
# subitems #
############

@router.post("/todolists/todoitems/subtodoitems/")
async def add_subitem(addSubTodoItem:AddSubTodoItem):
    subTodoItem = TodoItem(_id=ObjectId(),description=addSubTodoItem.description,subTodoItems=[],done=False)
    dictionary = subTodoItem.model_dump(by_alias=True)
    dictionary["_id"] = ObjectId(dictionary["_id"])

    todolists.find_one_and_update({
        "_id":ObjectId(addSubTodoItem.list_id),
        "todoItems._id":ObjectId(addSubTodoItem.item_id),
    },{
        "$push": {
            "todoItems.$.subTodoItems": dictionary
        }
    })
    return subTodoItem

@router.put("/todolists/todoitems/subtodoitems/done/")
async def toggle_subitem_done(updateSubTodoItem:UpdateSubTodoItem):
    result = todolists.find_one({
        # "_id":ObjectId(updateSubTodoItem.list_id),
        # "todoItems._id":ObjectId(updateSubTodoItem.item_id),
        "todoItems.subTodoItems._id": ObjectId(updateSubTodoItem.subitem_id) 
    },{
        "todoItems.subTodoItems.$":1
    })
    
    done_state = False

    if result and "todoItems" in result:
        subTodoItems = result["todoItems"][0]["subTodoItems"]
        subitem = next(
            (item for item in subTodoItems if item["_id"] == ObjectId(updateSubTodoItem.subitem_id)),
            None
        )
        print(subitem)
        done_state = subitem["done"]
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    
    new_done_state = not done_state

    result2 = todolists.update_one(
        {
            # "_id": ObjectId(updateSubTodoItem.list_id),  # Match the document
            # "todoItems._id": ObjectId(updateSubTodoItem.item_id),  # Match the specific todoItem
            "todoItems.subTodoItems._id": ObjectId(updateSubTodoItem.subitem_id)  # Match the specific subTodoItem
        },
        {
            "$set": {
                "todoItems.$[item].subTodoItems.$[subItem].done": new_done_state
            }
        },
        array_filters=[
            {"item._id": ObjectId(updateSubTodoItem.item_id)},  # Filter for the parent todoItem
            {"subItem._id": ObjectId(updateSubTodoItem.subitem_id)}  # Filter for the specific subTodoItem
        ]
    )


@router.delete("/todolists/todoitems/subtodoitems/{list_id}/{item_id}/{subitem_id}/")
async def delete_subitem(list_id:str, item_id:str, subitem_id:str):
    result = todolists.update_one(
        {
            "_id": ObjectId(list_id),  # Match the document
            "todoItems._id": ObjectId(item_id)  # Match the specific todoItem
        },
        {
            "$pull": {
                "todoItems.$.subTodoItems": {
                    "_id": ObjectId(subitem_id)  # Match the subTodoItem to remove
                }
            }
        }
    )

@router.put("/todolists/todoitems/subtodoitems/rename/")
async def rename_subitem(updateSubTodoItem:UpdateSubTodoItem):
    todolists.update_one(
        {
            # "_id": ObjectId(updateSubTodoItem.list_id),  # Match the document
            # "todoItems._id": ObjectId(updateSubTodoItem.item_id),  # Match the specific todoItem
            "todoItems.subTodoItems._id": ObjectId(updateSubTodoItem.subitem_id)  # Match the specific subTodoItem
        },
        {
            "$set": {
                "todoItems.$[item].subTodoItems.$[subItem].description": updateSubTodoItem.description
            }
        },
        array_filters=[
            {"item._id": ObjectId(updateSubTodoItem.item_id)},  # Filter for the parent todoItem
            {"subItem._id": ObjectId(updateSubTodoItem.subitem_id)}  # Filter for the specific subTodoItem
        ]
    )

def find_user_query(user_id:str):
    try:
        return users.find_one({"_id": ObjectId(user_id)})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exists")