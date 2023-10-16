import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uuid
import Database_Constants
import ast

#from cryptography.fernet import Fernet


class UserHandler:

    def __init__(self, debugMode : bool):
        self.__debugMode = debugMode
        self.__mongo = DB_init.InitializeGlobals(self.__debugMode)
        self.__mongo_url = self.__mongo.getMongoURI()  # Default MongoDB connection URL
        self.__database_name = self.__mongo.getDatabase_name  # Replace with your desired database name

        # Initialize the MongoDB client
        self.__client = self.__mongo.getClient()

        # Create or access the database
        self.__db = self.__mongo.getDatabase()

        self.__users = self.__mongo.getUsers()

    def addUser(self, criteria : dict):

        

        userDocument = {
            "userName": criteria.get('userName'),
            "password": criteria.get('password'),
            "userID" : criteria.get('userID'),
            "projects" : criteria.get('projects')
        }

        self.__users.insert_one(userDocument)


    def dropUser(self, userID : str):
        self.__users.delete_one( {"userID" : userID})


    def findUser(self, criteria : dict, fieldToReturn : dict):
        doesUserExist = False
        value = self.__users.find_one(criteria,fieldToReturn)
        if(value != None):
            doesUserExist = True

        return value, doesUserExist

    def editUser(self, criteria : dict, valuesToUpdate : dict):
        returnVal, doesUserExist = self.findUser(criteria,valuesToUpdate)
        if(doesUserExist == True):
            valuesToUpdate = { "$set": valuesToUpdate}
            self.__users.update_one(criteria, valuesToUpdate)
            returnVal, doesUserExist = self.findUser(criteria,None)
            return returnVal, doesUserExist
        else:
            return None, False


    def addTeam(self, userID : str , projectName : str):
        criteria = {'userID' : userID}
        fToReturn = {'projects' : 1, '_id' : 0}
        matched = self.findUser(criteria, fToReturn)
        mylist = ast.literal_eval(str(matched)[10:-1])

        mylist.append(projectName)

        update_operation = {'$set': {
            'projects' : mylist
        }}

        criteria = {'userID' : userID}

        self.__users.update_one(criteria, update_operation)


    def dropTeam(self, userID : str, projectName : str):
        criteria = {'userID' : userID}
        fToReturn = {'projects' : 1, '_id' : 0}
        matched = self.findUser(criteria, fToReturn)
        mylist = ast.literal_eval(str(matched)[10:-1])

        mylist.remove(projectName)

        update_operation = {'$set': {
            'projects' : mylist
        }}

        criteria = {'userName' : userID}

        self.__users.update_one(criteria, update_operation)

    def editTeam(self, userID : str, prevProjectName : str, newProjectName):
        criteria = {'userName' : userID}
        fToReturn = {'projects' : 1, '_id' : 0}
        matched = self.findUser(criteria, fToReturn)
        strippedMatched = str(matched)[13:-1]
        mylist = ast.literal_eval(strippedMatched)


        for i in range(len(mylist)):

            if mylist[i] == prevProjectName:
                mylist[i] = newProjectName
                

        update_operation = {'$set': {
            'projects' : mylist
        }}

        criteria = {'userName' : userID}

        self.__users.update_one(criteria, update_operation)

    
    def dropUserCollection(self):
        if(self.__debugMode == True):
            self.__users.drop()




        
        
        
        
