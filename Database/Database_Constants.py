import pymongo

class InitializeGlobals:

    def __init__(self):
        self.__database_name = "NumpyNinjasDB"
        self.__mongourl = "mongodb+srv://numpy_ninja:ninja461L@numpyninjasdb.jg4w9p9.mongodb.net/"
        self.__client = pymongo.MongoClient(self.__mongourl)


        self.__db = self.__client[self.__database_name]
        self.__users = self.__db.users
        self.__teams = self.__db.teams

    
    def getDatabase_name(self):
        return self.__database_name
    
    def getMongoURL(self):
        return self.__mongourl
    
    def getClient(self):
        return self.__client
    
    def getDatabase(self):
        return self.__db
    
    def getUsers(self):
        return self.__users
    
    def getTeams(self):
        return self.__teams