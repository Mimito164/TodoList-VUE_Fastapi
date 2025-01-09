def todolist_schema(todolist) -> dict:
    return {
        "id":str(todolist["_id"]),
        "name":todolist["name"],
        "todoItems":todolist["todoItems"]
    }

def todolists_schema(todolists) -> list:
    return [todolist_schema(todolist) for todolist in todolists]