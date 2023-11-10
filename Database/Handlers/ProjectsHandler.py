import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bcrypt
import DB_init
import ast
import HWSetHandler

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
        
        self.__hwHandler = HWSetHandler.HWSetHandler(debugMode)
        self.__hwHandler.initializeHWSet('Computers',140)
        self.__hwHandler.initializeHWSet('Servers',100)
        
    def checkExistingProject(self, projectID):
        #check to see if there is a project with the same id already
        doesProjectExist = False
        project = self.__Projects.find_one({"projectID" : projectID})
        if(project != None):
            doesProjectExist = True
        return doesProjectExist
    def createProject(self, criteria : dict):
        projectAdded = False
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
    def joinProject(self, criteria : dict):
        #if there is already an existing project, update the project if the user is different

        _err = None
        projectJoined = False
        projectID = criteria["projectID"]
        existingProject = self.__Projects.find_one({"projectID" : criteria["projectID"]})
        if existingProject == None:
            return projectJoined, "Project does not exist"
        existingUsers = existingProject.get("users", [])
        if criteria["userName"] in existingUsers:
            return projectJoined, "User is already in Project"
        #gets list of users for project
        existingUsers.append(criteria["userName"])
        #update the username list in the document
        existingProject["users"] = existingUsers
        self.__Projects.update_one({"projectID" : projectID}, {"$set" : existingProject})

        newProject = self.__Projects.find_one({"projectID" : criteria["projectID"]})
        newUsers = newProject.get("users", [])
        if criteria["userName"] in newUsers:
            projectJoined = True
            return projectJoined, _err
        return projectJoined, "User was not added to Project"


    def isUserInProject(self, criteria : dict):
        #check to see if user is in the project
        username = criteria["username"]
        projectID = criteria["projectID"]
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
        for project in self.__Projects.find({"users": username}, {"_id": 0}):
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

    def checkOutHardwareSet(self, criteria : dict):
        
        newHWSet_Val = self.__hwHandler.checkOutHWSet(criteria)
        x = self.__Projects.find_one({'projectID':criteria['projectID']})
        setToUpdate = None

        if criteria['hwSetID'] == 'Computers': setToUpdate = 'Computers_CheckedOut'
        else: setToUpdate = 'Servers_CheckedOut'

        updatedHWSet = x[setToUpdate] + newHWSet_Val
        self.__Projects.update_one({'projectID':x['projectID']},{'$set':{setToUpdate:updatedHWSet}})
        


    def checkInHardwareSet(self, criteria : dict):
        
        newHWSet_Val = self.__hwHandler.checkInHWSet(criteria)
        x = self.__Projects.find_one({'projectID':criteria['projectID']})
        setToUpdate = None

        if criteria['hwSetID'] == 'Computers': setToUpdate = 'Computers_CheckedOut'
        else: setToUpdate = 'Servers_CheckedOut'

        updatedHWSet = x[setToUpdate] - newHWSet_Val
        self.__Projects.update_one({'projectID':x['projectID']},{'$set':{setToUpdate:updatedHWSet}})
        
    def displayHardware(self):
        HWSet1Availability, _err1 = self.__hwHandler.getHWSetAvailability({'hwSetID' : 'Computers'})
        HWSet2Availability, _err2 = self.__hwHandler.getHWSetAvailability({'hwSetID' : 'Servers'})
        HWSet1Capacity, _err3 = self.__hwHandler.getHWSetQty({'hwSetID' : 'Computers'})
        HWSet2Capacity, _err4 = self.__hwHandler.getHWSetQty({'hwSetID' : 'Servers'})
        _err = _err1 and _err2 and _err3 and _err4
        return HWSet1Availability, HWSet2Availability, HWSet1Capacity, HWSet2Capacity, _err

 

        
        

