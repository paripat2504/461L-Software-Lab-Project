import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bcrypt
import DB_init
import ast
import HWSetHandler

hwHandler = HWSetHandler.HWSetHandler(debugMode)
hwHandler.initializeHWSet('Computers',140)
hwHandler.initializeHWSet('Servers',100)

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
        

        
    def checkExistingProject(self, projectID):
        #check to see if there is a project with the same id already
        doesProjectExist = False
        project = self.__Projects.find_one({"projectID" : projectID})
        if(project != None):
            doesProjectExist = True
        return doesProjectExist
    def createProject(self, criteria : dict):
        projectAdded = False
        _err = "Project with this name already exists"
        doesProjectExist = self.checkExistingProject(criteria['projectID'])
        _err = "Project already exists with that projectID"
        if doesProjectExist == False:    
            projectDocument = {
                "projectName": criteria["projectName"],
                "projectDescription": criteria["projectDescription"],
                "projectID" : criteria['projectID'],
                "users" : [criteria["userName"]],
                "Computers_CheckedOut" : 0,
                "Servers_CheckedOut" : 0
            }
            self.__Projects.insert_one(projectDocument)
            projectAdded = True
            _err = None
        return projectAdded, _err
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
    #method to change number of checkedout hardware sets for each project
    def updateHardwareSets(self, criteria : dict):
        #update checkedOutFields in Project
        projectID = criteria["id"]
        HW1 = criteria["HardwarSet1"]
        HW2 = criteria["HardwareSet2"]
        existingProject = self.__Projects.find_one({"projectID" : criteria["projectID"]})
        existingProject["Computers"] = HW1
        existingProject["Servers"] = HW2
        self.__Projects.update_one({"projectID" : projectID}, {"$set" : existingProject})
    def isUserInProject(self, criteria : dict):
        #check to see if user is in the project
        username = criteria["username"]
        projectID = criteria["id"]
        existingProject = self.__Projects.find_one({"projectID" : criteria["projectID"]})
        listOfUsers = existingProject["users"]
        if username in listOfUsers:
            return True
        else: 
            return False
    def UserProjectIds(self, username):
        #method to return all the projectIDs the user is currently a part of 
        user_projects = []
        _err = None
        for project in self.__Projects.find({"users": username}):
            projectID = project["projectID"]
            user_projects.append(projectID)
        if len(user_projects) == 0:
            _err = "Username is not in any projects"
        return user_projects, _err
    def returnUserProjects(self, username):
        _err = None
        user_projects = []
        for project in self.__Projects.find({"users": username}):
            user_projects.append(project)
        if len(user_projects) == 0:
            _err = "Username is not in any projects"
        return user_projects, _err
    def removeUserFromProject(self, criteria : dict):
        username = criteria['username']
        projectID = criteria['projectID']
        project = self.__Projects.find_one({"projectID": projectID})
        _err = None
        if project is not None:
            users = project.get("users", [])
            if username in users:
                users.remove(username)
                project["users"] = users
                self.__Projects.update_one({"projectID": projectID}, {"$set": project})
                return True, _err  # User removed successfully
        _err = "Project or User is not found"
        return False, _err  # Project or user not found

        
        
        
