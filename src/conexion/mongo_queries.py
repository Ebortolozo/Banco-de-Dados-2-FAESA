import pymongo

class MongoQueries:
    def __init__(self):
        pass

    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        self.mongo_client = pymongo.MongoClient("localhost", 27017)
        self.db = self.mongo_client["labdatabase"]

    def close(self):
        self.mongo_client.close()