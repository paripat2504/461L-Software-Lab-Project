import sys
import os

from flask import jsonify
from ProjectsHandler import ProjectHandler

ProjHandler = ProjectHandler()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bcrypt
# import DB_init
import ast





# class HWSetHandler:


#     def __init__(self, debugMode : bool = True):
#         x =4
#         # self.__mongo = DB_init.InitializeGlobals(self.__debugMode)
#         # self.__mongo_url = self.__mongo.getMongoURI()  # Default MongoDB connection URL
#         # self.__database_name = self.__mongo.getDatabase_name  # Replace with your desired database name

#         # # Initialize the MongoDB client
#         # self.__client = self.__mongo.getClient()

#         # # Create or access the database
#         # self.__db = self.__mongo.getDatabase()

#         # self.__HWSet = self.__mongo.getProjects()

#     # def findHWSet(self, name):
#     #     _err :str
#     #     if self.__HWSet.find_one({'name' : name},{'_id':0})[1] == False:
#     #         _err = 'HW Set Not Found'
#     #         return None, _err
        
#     #     else:
#     #         returnVal = self.__HWSet.find_one({'name' : name},{'_id':0})
#     #         return returnVal, None    

#     # def addHWSet(self,name: str,availability: int):
        
#     #     self.__HWSet.insert_one({'name' : name, 'availability' : availability, 'qty' : availability})



#     # def checkInHardware(self, projID : str, qty : int):
#     #     x = 5
#     #     self.__availability += qty

        



        




#     # def checkOutHardware(self, projID : str, qty : int):
#     #     x=2

