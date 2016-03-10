import pymongo

__author__ = 'edijemeni'

#Database is just an object. Has the properties of an object
class Database(object):

    #All database will have the same URI and database

    #Step 1 - Get the mongoDB address!!!
    URI = "mongodb://127.0.0.1:27017"

    #Step 2 - Get the database
    DATABASE = None

    # Create the initalise method you dont want __init__ !!
    # Staticmethod is saying I dont want to use self!
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["fullstack"]

    # How do I insert a JSON document in a collection on mongoDB using Python
    # e.g how do I insert a blog post into a blog collection in full stack database
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    # How do I retrieve all the data in a collection on a mongoDB database using python
    # e.g how do I retrive info about all the blog post from fullstack database
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # How do I retrieve a specific document in a collection?
    # e.g how do I retreive blog x in the blog collection in fullstack database?
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    # HS, please teach me how to update the website
    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query,data, upsert=True)

    # HS, please help me delete from the database
    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)