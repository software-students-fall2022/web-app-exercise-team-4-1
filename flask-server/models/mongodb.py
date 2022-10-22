from pymongo import MongoClient
from bson.json_util import dumps, loads

class Database(object):

    url = "mongodb+srv://leo:<leo>@cluster0.pmplyl1.mongodb.net/?retryWrites=true&w=majority"
    database=None
    
    @staticmethod
    def initialize():
        connection= MongoClient(Database.url)
        Database.database = connection["db"]

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)

    @staticmethod
    def find(collection, query=""):
        return dumps(Database.database[collection].find(query))

    @staticmethod
    def find_single(collection, query):
        return dumps(Database.database[collection].find_one(query))

    @staticmethod
    def delete(collection, query):
        return Database.database[collection].delete_one(query)

    @staticmethod
    def update(collection, query):
        return Database.database[collection].update_one(query)
    @staticmethod
    def close():
        Database.database.close()
