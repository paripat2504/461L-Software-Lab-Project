import pymongo
import UserHandler
import Database_Constants
import datetime

# Replace these with your MongoDB connection details

mongo = Database_Constants.InitializeGlobals()


mongo_url = mongo.getMongoURL()  # Default MongoDB connection URL

users = mongo.getUsers()


UserHandler.addUser("newUser", "userLogin", "passwd", ["Numpy Ninjas", "Team"])

val = 5
