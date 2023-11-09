import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DB_init


class HWSetHandler:
    def __init__(self, debugMode : bool = True):
        x =4
        self.__mongo = DB_init.InitializeGlobals(debugMode)
        self.__mongo_url = self.__mongo.getMongoURI()  # Default MongoDB connection URL
        self.__database_name = self.__mongo.getDatabase_name  # Replace with your desired database name

        # Initialize the MongoDB client
        self.__client = self.__mongo.getClient()

        # Create or access the database
        self.__db = self.__mongo.getDatabase()

        self.__HWSet = self.__mongo.getHWSets()

    def findHWSet(self, hwSetID : str):
        doesHWSetExist = False
        returnVal = self.__HWSet.find_one({'hwSetID' : hwSetID},{'_id':0})
        if returnVal != None:
            doesHWSetExist = True


        return returnVal, doesHWSetExist
    

    def initializeHWSet(self,hwSetID: str,availability: int):
        val , exists = self.findHWSet(hwSetID)
        _err = None
        if(exists == False):
            self.__HWSet.insert_one({'hwSetID' : hwSetID, 'availability' : availability, 'qty' : availability})
        else:
            _err = 'Hardware Set with this ID already exists'

        return _err
            


    def checkInHardware(self, projID : str, qty : int):
        x = 5
        self.findHWSet(projID)

