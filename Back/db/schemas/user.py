def user_schema(user):
    return {
        "id":str(user["_id"]),
        "todolistIDs":user["todolistIDs"],
        "wallet":user["wallet"]
    }

def users_schema(users: list) -> list:
    return [user_schema(user) for user in users]