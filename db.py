import os
from dotenv import load_dotenv
import pymongo

load_dotenv()
password = os.getenv('DBPWD')
driver = os.getenv('DBDRIVER')
user = os.getenv('DBUSER')
host = os.getenv('DBHOST')


def connect_db():
    print('connecting to MongoDB...')
    client = pymongo.MongoClient(f'{driver}://{user}:{password}@{host}/?retryWrites=true&w=majority')
    return client


def get_collection(client, collection_name):
    db = client.development
    collection = db[collection_name]
    return collection


def get_all_documents(client, collection, user_name):
    documents = list(collection.find({"userName": user_name}))
    return documents


def get_latest_document(client, collection, user_name):
    documents = list(collection.find({"userName": user_name}))
    return documents[-1]


def get_codeparams_from_time(client, collection, user_name, executed_time):
    document = collection.find({
        "userName": user_name,
        "executedAt": executed_time
        })
    return document[0]


def test_db():
    client = connect_db()
    collection = get_collection(client, "processed")
    print(collection.distinct('userName'))