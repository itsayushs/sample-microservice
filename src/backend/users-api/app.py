import uvicorn, os
from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
async def root():
    db_uri = os.getenv('DB_URI')  or 'localhost'
    db_username = os.getenv('DB_USER') or 'root'
    db_pass = os.getenv('DB_PASS') or 'admin'

    db_client = MongoClient(db_uri,
                            username=db_username,
                            password=db_pass)
    userdb = db_client['usersdb']
    user_collection = userdb['users']
    userdata = user_collection.find({},{"_id": 0})
    db_client.close()
    data = [users for users in userdata]
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
