import pymongo
import json

class InitializeGlobals:

    def __init__(self, debugMode : bool):
        db_credsfile = open('Database\DB_creds.json', 'r')
        db_creds = json.load(db_credsfile)

        self.__database_name = db_creds.get('mongodb_name')
        self.__mongoDBuri = db_creds.get('mongodb_uri')
        if(debugMode == True):
            self.__database_name = db_creds.get('testDB_name')
            self.__mongoDBuri = db_creds.get('testDB_uri')


        self.__client = pymongo.MongoClient(self.__mongoDBuri)


        self.__db = self.__client[self.__database_name]
        self.__users = self.__db.users
        self.__teams = self.__db.teams

    
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
    
    def getTeams(self):
        return self.__teams