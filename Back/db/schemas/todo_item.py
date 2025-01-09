def todolist_item_schema(todolist_item) -> dict:
    return {
        "id":str(todolist_item["_id"]),
        "description":todolist_item["description"],
        "subTodoItems":[todolist_item_schema(subTodo) for subTodo in todolist_item["subTodoItems"]],
        "status": todolist_item["status"]
    }

def todolist_items_schema(todolist_items) -> list:
    return [todolist_item_schema(todolist_item) for todolist_item in todolist_items]