from fastapi import FastAPI, HTTPException
from app.models import User
from ..db import database
from db.session import SessionLocal
app = FastAPI()

@app.post("/users/", response_model=User)
async def create_user(user: User):
    query = User.insert().values(
        username=user.username,
        email=user.email
    )
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = User.select().where(User.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    query = User.update().where(User.c.id == user_id).values(
        username=user.username,
        email=user.email
    )
    await database.execute(query)
    return {**user.dict(), "id": user_id}

