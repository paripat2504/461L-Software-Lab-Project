import uuid
import Database_Constants
import ast

from cryptography.fernet import Fernet



mongo = Database_Constants.InitializeGlobals()


mongo_url = mongo.getMongoURL()  # Default MongoDB connection URL
database_name = mongo.getDatabase_name  # Replace with your desired database name

# Initialize the MongoDB client
client = mongo.getClient()

# Create or access the database
db = mongo.getDatabase()

users = mongo.getUsers()

def addUser(userName : str, userID : str, password : str, projects):

    

    userDocument = {
        "userName": userName,
        "password": password,
        "userID" : userID,
        "projects" : projects
    }

    users.insert_one(userDocument)


def dropUser(userID):
    users.delete_one( {"userID" : userID})


def addTeam(userID : str , projectName : str):
    criteria = {'userID' : userID}
    fToReturn = {'projects' : 1, '_id' : 0}
    matched = findUser(criteria, fToReturn)
    mylist = ast.literal_eval(str(matched)[10:-1])

    mylist.append(projectName)

    update_operation = {'$set': {
        'projects' : mylist
    }}

    criteria = {'userID' : userID}

    users.update_one(criteria, update_operation)


def dropTeam(userID : str, projectName : str):
    criteria = {'userID' : userID}
    fToReturn = {'projects' : 1, '_id' : 0}
    matched = findUser(criteria, fToReturn)
    mylist = ast.literal_eval(str(matched)[10:-1])

    mylist.remove(projectName)

    update_operation = {'$set': {
        'projects' : mylist
    }}

    criteria = {'userName' : userID}

    users.update_one(criteria, update_operation)

def editTeam(userID : str, prevProjectName : str, newProjectName):
    criteria = {'userName' : userID}
    fToReturn = {'projects' : 1, '_id' : 0}
    matched = findUser(criteria, fToReturn)
    strippedMatched = str(matched)[13:-1]
    mylist = ast.literal_eval(strippedMatched)


    for i in range(len(mylist)):

        if mylist[i] == prevProjectName:
            mylist[i] = newProjectName
            

    update_operation = {'$set': {
        'projects' : mylist
    }}

    criteria = {'userName' : userID}

    users.update_one(criteria, update_operation)



def findUser(criteria, fieldToReturn):
    if(fieldToReturn != None):
        value = users.find_one(criteria,fieldToReturn)

        return value
    
    else:
        value = users.find_one(criteria)
        return value
    
    

