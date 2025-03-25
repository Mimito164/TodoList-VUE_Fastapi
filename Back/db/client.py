from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv('MONGODB_URI')

client = MongoClient(uri, server_api=ServerApi('1')).todolist
users = client.users
todolists = client.todolists