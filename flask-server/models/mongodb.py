from pymongo import MongoClient
from bson.json_util import dumps, loads

class Database(object):

    url = "mongodb+srv://admin:admin123@cluster0.b6toxnx.mongodb.net/?retryWrites=true&w=majority"
    database=None
    client=None
    
    @staticmethod
    def initialize():
        connection= MongoClient(Database.url)
        try:
            connection.admin.command('ping')
            Database.client=connection
            Database.database = connection["db"]
            print(' *', 'Connected to MongoDB!') 
        except Exception as e:
            print(' *', "Failed to connect to MongoDB at")
            print('Database connection error:', e)

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)

    @staticmethod
    def find(collection, query="", field=""):
        return (Database.database[collection].find(query,field))

    @staticmethod
<<<<<<< HEAD
    def find_single(collection, query):
        return dumps(Database.database[collection].find_one(query))
=======
    def find_single(collection,query,field=""):
        return (Database.database[collection].find_one(query,field))
>>>>>>> cfd45e5138180ba14fd03a09cad6ad09c62674dd

    @staticmethod
    def delete(collection, query):
        return Database.database[collection].delete_one(query)

    @staticmethod
    def update(collection, search, query):
        return Database.database[collection].update_one(search,query)

    @staticmethod
    def count(collection, query):
        return Database.database[collection].count_documents(query)

    @staticmethod
    def close():
        Database.client.close()

