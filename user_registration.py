from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

# In-memory storage for users
users_db = []

class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

@app.post("/register")
def register_user(request: RegisterRequest):
    # Check if email already exists
    for user in users_db:
        if user["email"] == request.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    new_user = {
        "username": request.username,
        "email": request.email,
        "password": request.password  # ⚠️ In real-world apps, NEVER store plain passwords
    }
    users_db.append(new_user)
    return {"message": "User registered successfully!", "user": request.username}

# Bonus: fetch all registered users
@app.get("/users")
def get_users():
    return {"registered_users": users_db}
