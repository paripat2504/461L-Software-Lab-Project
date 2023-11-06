import sys
import os

from flask import jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bcrypt
import DB_init
import ast

#from cryptography.fernet import Fernet


class UserHandler:

    def __init__(self, debugMode : bool = True):
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
        userAdded = False
        password = criteria['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password,bcrypt.gensalt())
        _err = "User already exists with that username or userID"



        if self.findUser({"userName": criteria['userName']},{})[1] == False or self.findUser({'userID': criteria['userID']},{})[1] == False:
            hashed_password = bcrypt.hashpw(password,bcrypt.gensalt())
            userAdded = True
            _err =  None  
            userDocument = {
                "userName": criteria["userName"],
                "password": hashed_password,
                "userID" : criteria['userID'],
                "projects" : []
            }

            self.__users.insert_one(userDocument)
         

        return userAdded, _err


    def dropUser(self, userID : str):
        self.__users.delete_one( {"userID" : userID})

    def validateUser(self, login : dict):
        attemptedLogin = login['password'].encode('utf-8')
        validLogin : bool = False
        loginDict = {'userID':login["userID"]}
        _err = "Incorrect UserID or Password"

        retrievedDict, exists = self.findUser(loginDict, {'password':1,'_id':0})
        if exists == True:
            retrievedPass = retrievedDict['password']

            if bcrypt.checkpw(attemptedLogin,retrievedPass):
                validLogin = True



        return validLogin, _err

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


    
    def resetUserCollection(self):
        if(self.__debugMode == True):
            self.__users.delete_many({})




