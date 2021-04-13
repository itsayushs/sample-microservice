import pymongo, os
import json

def seedUserData(user_collection):
    with open('backend/users-api/data.json') as user_data:
        data = json.load(user_data)
    response = user_collection.insert_many(data)
    return response


if __name__ == "__main__":
    db_uri = os.getenv('DB_URI')  or 'localhost'
    db_username = os.getenv('DB_USER') or 'root'
    db_pass = os.getenv('DB_PASS') or 'admin'

    db_client = pymongo.MongoClient(db_uri,
                            username=db_username,
                            password=db_pass)

    userdb = db_client['usersdb']
    user_collection = userdb['users']

    collist = userdb.list_collection_names()
    if "users" in collist:
        print("The collection exists! No seeding needed")
    else: 
        seedUserData(user_collection)
        print("User data added!")
    db_client.close()
