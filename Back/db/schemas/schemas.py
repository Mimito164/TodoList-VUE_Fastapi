def user_schema(user) -> dict:
    return {
        "id":str(user["_id"]),
        "wallet":user["wallet"]
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]