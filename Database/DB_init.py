import pymongo
import json

class InitializeGlobals:

    def __init__(self, debugMode : bool):
        # db_credsfile = open('Database\DB_creds.json', 'r')
        # db_creds = json.load(db_credsfile)
        # db_credsfile.close()
        self.__database_name = "NumpyNinjasDB"
        self.__mongoDBuri = "mongodb+srv://numpy_ninja:ninja461L@numpyninjastestdb.jg4w9p9.mongodb.net/"
        if(debugMode == True):
            self.__database_name = "NumpyNinjasTestDB"
            self.__mongoDBuri = "mongodb+srv://numpy_ninja:ninja461L@numpyninjastestdb.jg4w9p9.mongodb.net/"


        self.__client = pymongo.MongoClient(self.__mongoDBuri)


        self.__db = self.__client[self.__database_name]
        self.__users = self.__db.users
        self.__Projects = self.__db.Projects
        self.__HWSet = self.__db.HWSet
    
    def getDatabase_name(self):
        return self.__database_name
    
    def getMongoURI(self):
        return self.__mongoDBuri
    
    def getClient(self):
        return self.__client
    
    def getDatabase(self):
        return self.__db
    
    def getUsers(self):
        return self.__users
    
    def getProjects(self):
        return self.__Projects
    
    def getHWSets(self):
        return self.__HWSet
    