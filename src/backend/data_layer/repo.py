import json
from pymongo import MongoClient

import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

db_usr  = os.getenv('DB_USR')
db_pwd  = os.getenv('DB_PWD')
db_host = os.getenv('DB_HOST')

class StoryRepository:
    def __init__(self, use_database=False):
        self.use_database = use_database

    def get_stories(self):
        if self.use_database:
            # Create mongodb connection
            uri = f"mongodb+srv://{db_usr}:{db_pwd}@{db_host}"
            # Create a new client and connect to the server
            client = MongoClient(uri)
            # Send a ping to confirm a successful connection
            try:
                client.admin.command('ping')
                print("Pinged your deployment. You successfully connected to MongoDB!")
            except Exception as e:
                print(e)

            # Create a database
            db = client['code-tales']
            # Create a collection
            stories_db = db['stories']
            # TODO Fetch stories from the database

            pass
        else:
            # Fetch stories from local files
            with open('src/data/stories.json', 'r') as f:
                stories = json.load(f)
            return stories
            
