import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bcrypt
import DB_init
import ast

class ProjectHandler:
    def __init__(self, debugMode : bool = True):
        self.__debugMode = debugMode
        self.__mongo = DB_init.InitializeGlobals(self.__debugMode)
        self.__mongo_url = self.__mongo.getMongoURI()  # Default MongoDB connection URL
        self.__database_name = self.__mongo.getDatabase_name  # Replace with your desired database name

        # Initialize the MongoDB client
        self.__client = self.__mongo.getClient()

        # Create or access the database
        self.__db = self.__mongo.getDatabase()

        self.__Projects = self.__mongo.getProjects()
    def createProject(self, criteria : dict):
        projectAdded = False
        projectDocument = {
            "projectName": criteria["projectName"],
            "projectDescription": criteria["description"],
            "projectID" : criteria['id'],
            "users" : [criteria["userName"]],
            "HardwareSet1CheckedOut" : 0,
            "HardwareSet1CheckedOut" : 0
        }
        self.__Projects.insert_one(projectDocument)
    def UseExistingProject(self, criteria : dict):
        #if there is already an existing project, update the project if the user is different
        projectID = criteria["id"]
        existingProject = self.__Projects.find_one({"projectID" : criteria["projectID"]})
        existingUsers = existingProject.get("users", [])
        #gets list of users for project
        existingUsers.append(criteria["username"])
        #update the username list in the document
        existingProject["users"] = existingUsers
        self.__Projects.update_one({"projectID" : projectID}, {"$set" : existingProject})
    def checkExistingProject(self, projectID):
        #check to see if there is a project with the same id already
        doesProjectExist = False
        project = self.__Projects.find_one("projectID" : projectID)
        if(project != None):
            doesProjectExist = True
        return doesProjectExist
    #method to change number of checkedout hardware sets for each project
    def checkOutHardwareSets(self, criteria : dict):
        #update checkedOutFields in Project
        projectID = criteria["id"]
        HW1 = criteria["HardwarSet1"]
        HW2 = criteria["HardwareSet2"]
        existingProject = self.__Projects.find_one({"projectID" : criteria["projectID"]})
        existingProject["HardwareSet1CheckedOut"] = HW1
        existingProject["HardwareSet2CheckedOut"] = HW2
        self.__Projects.update_one({"projectID" : projectID}, {"$set" : existingProject})
    def isUserInProject(self, criteria : dict):
        #check to see if user is in the project
        username = criteria["username"]
        projectID = criteria["id"]
        existingProject = self.__Projects.find_one({"projectID" : criteria["projectID"]})
        listOfUsers = existingProject["users"]
        if username in listofUsers:
            return True
        else: 
            return False