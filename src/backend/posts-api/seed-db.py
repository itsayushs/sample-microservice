import pymongo, os
import json

def seedUserData(post_collection):
    with open('backend/posts-api/data.json') as user_data:
        data = json.load(user_data)
    response = post_collection.insert_many(data)
    return response


if __name__ == "__main__":
    db_uri = os.getenv('DB_URI')  or 'localhost'
    db_username = os.getenv('DB_USER') or 'root'
    db_pass = os.getenv('DB_PASS') or 'admin'

    db_client = pymongo.MongoClient(db_uri,
                            username=db_username,
                            password=db_pass)

    postdb = db_client['postsdb']
    post_collection = postdb['posts']

    collist = postdb.list_collection_names()
    if "posts" in collist:
        print("The collection exists! No seeding needed")
    else: 
        seedUserData(post_collection)
        print("Posts data added!")
    db_client.close()
