from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1: {"name": "John", "age": "30"},
    2: {"name": "Jane", "age": "25"},
    3: {"name": "Alice", "age": "28"}
}


class User(BaseModel):
    name: str
    age: int

@app.put("/users/{user_id}")
def user_update(user_id: int, user: User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message": "User updated successfully"}
    return {"message": "User not found"}


@app.delete("/users/{user_id}")
def user_delete(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    return {"message": "User not found"}