# Eric Shadwick Week 4 assignment
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # The MongoClient gives access to the MongoDB databases and
        # collections. This is hard-wired to use the aac database, the
        # animals collection, and the port the AAC environment uses.
        #
        # Credentials are now passed in by the caller (the dashboard)
        # rather than hardcoded, so the username/password entered at the
        # login prompt are what authenticate against MongoDB.
        #
        # Connection Variables
        #
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=%s' % (username, password, HOST, PORT, DB))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        """
        Insert a document into the animals collection.
        :param data: dictionary of key/value pairs to insert
        :return: True if the insert succeeds, otherwise False
        """
        if data is not None:
            try:
                # insert_one returns a result object; its acknowledged
                # flag confirms the server accepted the write.
                result = self.database.animals.insert_one(data)
                return result.acknowledged
            except PyMongoError as e:
                # Catch driver-level errors so a failed write returns
                # False rather than crashing the caller.
                print(f"An error occurred during insert: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        """
        Query for documents in the animals collection.
        :param query: dictionary of key/value lookup pair(s)
        :return: list of matching documents, or an empty list
        """
        if query is not None:
            try:
                # find() returns a cursor; wrapping it in list() gives the
                # caller a concrete, reusable result set.
                results = list(self.database.animals.find(query))
                return results
            except PyMongoError as e:
                print(f"An error occurred during query: {e}")
                return []
        else:
            raise Exception("Nothing to search, because query parameter is empty")

    # Create method to implement the U in CRUD.
    def update(self, query, new_values):
        """
        Update document(s) in the animals collection.
        :param query: dictionary of key/value lookup pair(s) to match
        :param new_values: dictionary of update operators/values
                           (for example, {"$set": {...}})
        :return: the number of documents modified
        """
        if query is not None and new_values is not None:
            try:
                # update_many changes every document matching the query;
                # modified_count reports how many were actually changed.
                result = self.database.animals.update_many(query, new_values)
                return result.modified_count
            except PyMongoError as e:
                # Catch driver-level errors so a failed update returns
                # 0 rather than crashing the caller.
                print(f"An error occurred during update: {e}")
                return 0
        else:
            raise Exception("Nothing to update, because query or new_values parameter is empty")

    # Create method to implement the D in CRUD.
    def delete(self, query):
        """
        Remove document(s) from the animals collection.
        :param query: dictionary of key/value lookup pair(s) to match
        :return: the number of documents removed
        """
        if query is not None:
            try:
                # delete_many removes every document matching the query;
                # deleted_count reports how many were removed.
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            except PyMongoError as e:
                # Catch driver-level errors so a failed delete returns
                # 0 rather than crashing the caller.
                print(f"An error occurred during delete: {e}")
                return 0
        else:
            raise Exception("Nothing to delete, because query parameter is empty")