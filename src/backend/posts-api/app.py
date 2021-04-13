import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests, pymongo, os

app = FastAPI()

def getUsers(postId):
    try:
        user_data = requests.get('http://localhost:8000/users')
        post_author = []
        for user in user_data.json():
            if postId in user['postId']:
                post_author.append(str(user['name']+" "+user['lname']))
        return post_author
    except:
        return []

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/post/2")
async def root():
    db_uri = os.getenv('DB_URI')  or 'localhost'
    db_username = os.getenv('DB_USER') or 'root'
    db_pass = os.getenv('DB_PASS') or 'admin'
    db_client = pymongo.MongoClient(db_uri,
                            username=db_username,
                            password=db_pass)

    postdb = db_client['postsdb']
    post_collection = postdb['posts']
    posts = post_collection.find({},{"_id": 0})
    db_client.close()
    post_id = 2
    response = [post for post in posts if post['id'] == post_id][0]
    authors = getUsers(post_id)
    if not authors:
        return {'statuscode': 404, 'data': 'nodata'}
    else:
        response['authors'] = authors
        return {'statuscode': 200, 'data': response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)