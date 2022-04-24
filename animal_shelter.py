from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37230' % (username, password))
        self.database = self.client['users']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. 
    def read(self, search):
        #checks if data is empty (null)
        if search is not None:
            result = self.database.animals.find(search)
            return result
        else:
            raise Exception("Nothing to search, because data parameter is empty")
            return Exception
        
# Create method to implement the U in CRUD. 
    def update(self, query, newValues):
        #checks if query is empty (null)
        if query and newValues is not None:
            updatedResult = self.database.animals.update(query, newValues)
            return updatedResult
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return Exception

# Create method to implement the D in CRUD. 
    def delete(self, delQuery):
        #checks if query is empty (null)
        if delQuery is not None:
            deletedResult = self.database.animals.delete_one(delQuery)
            return deletedResult
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            return Exception