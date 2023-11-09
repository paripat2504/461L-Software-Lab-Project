from re import T
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DB_init


class HWSetHandler:
    def __init__(self, debugMode : bool = True):
        x =4
        self.__debugMode = debugMode
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
    
    def getHWSetAvailability(self, criteria : dict):
         x, _err = self.findHWSet(criteria['hwSetID'])
         return x['availability']

    def getHWSetQty(self, criteria : dict):
         x, _err = self.findHWSet(criteria['hwSetID'])
         return x['qty']
    
    def setHWSetAvailability(self, criteria : dict):
        self.__HWSet.update_one({'hwSetID':criteria['hwSetID']},{"$set" : {'availability':criteria['amtToSet']}})
    

    def initializeHWSet(self,hwSetID: str,availability: int):
        val , exists = self.findHWSet(hwSetID)
        _err = None
        if(exists == False):
            self.__HWSet.insert_one({'hwSetID' : hwSetID, 'availability' : availability, 'qty' : availability})
        else:
            _err = 'Hardware Set with this ID already exists'

        return _err
            


    def checkOutHWSet(self,criteria : dict):
        availableHWSet = self.getHWSetAvailability({'hwSetID':criteria['hwSetID']})
        newHWSetVal = 0

        if int(criteria['amountRequested']) > availableHWSet:
            self.setHWSetAvailability({'hwSetID':criteria['hwSetID'],'amtToSet':0})
            newHWSetVal = availableHWSet
        else:
            availableHWSet -= int(criteria['amountRequested'])
            self.setHWSetAvailability({'hwSetID':criteria['hwSetID'],'amtToSet':availableHWSet})
            newHWSetVal = int(criteria['amountRequested'])

        return newHWSetVal

    def checkInHWSet(self,criteria : dict):
        HWSetqty = self.getHWSetQty({'hwSetID':criteria['hwSetID']})
        availableHWSet = self.getHWSetAvailability({'hwSetID':criteria['hwSetID']})
        newHWSetVal = 0
        comparator = int(criteria['amountRequested']) + availableHWSet
        if comparator > HWSetqty:
            self.setHWSetAvailability({'hwSetID':criteria['hwSetID'],'amtToSet':HWSetqty})
            newHWSetVal = 0
        else:
            availableHWSet += int(criteria['amountRequested'])
            self.setHWSetAvailability({'hwSetID':criteria['hwSetID'],'amtToSet':availableHWSet})
            newHWSetVal = int(criteria['amountRequested'])
        
        return newHWSetVal
        
        

# h = HWSetHandler(True)
# x = h.checkOutHWSet({'hwSetID':'Servers','amountRequested':20})
# x = h.checkInHWSet({'hwSetID':'Servers','amountRequested':20})
# y = 4
