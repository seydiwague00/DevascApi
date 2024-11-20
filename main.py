from typing import List
from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException

from models import User, Gender, Role

app = FastAPI()

# conn = psycopg2.connect(
#     dbname="devasc",
#     user="postgres",
#     password="postgres",
#     host="localhost",
#     port="5432"
# )
#
# # Creation de curseur
# cur = conn.cursor()
#
# # Execution de la requete
# cur.execute("SELECT version();")
#
# # Recuperer les resultats
# record = cur.fetchone()
# print(f"Version de postgreSQL : {record}")
#
# cur.close()
# conn.close()

db: List[User] = [
    User(
        id=UUID("b5e5ec80-889c-4148-bf71-f6834d8ed90d"),
        first_name="Alex",
        last_name="jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID("c0075974-9237-4185-9724-d89425183c52"),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.student]
    )
]


@app.get("/")
async def root():
    return {"message": "Hello Shidei"}


@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users/add_user")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.get("/api/v1/users/get_user/{user_id}")
async def get_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/v1/users/delete_user/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"id": user_id}
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/v1/users/update_user/{user_id}")
async def update_user(user_id: UUID, user_param: User):
    for user in db:
        if user.id == user_id:
            user.first_name = user_param.first_name
            user.last_name = user_param.last_name
            user.gender = user_param.gender
            user.roles = user_param.roles
            return user
        raise HTTPException(status_code=404, detail="User not found")
