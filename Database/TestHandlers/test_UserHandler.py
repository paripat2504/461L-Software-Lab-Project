import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Handlers import UserHandler
import Database_Constants
import unittest
import pymongo

# Replace these with your MongoDB connection details

mongo = Database_Constants.InitializeGlobals()
mongo_url = mongo.getMongoURL()  # Default MongoDB connection URL
users = mongo.getUsers()



class testUserHandler(unittest.TestCase):
    def testAddAndDropUser(self):
        criteria = {'userName' : 'newUser', 'userID' : 'user1' , 'password' : 'passwd' , 'projects' : []}
        UserHandler.addUser(criteria)
        returnVal, userExists = UserHandler.findUser({'userID' : "user1"}, {'userID' : 1 , '_id' : 0})
        self.assertEqual({'userID' : 'user1'},returnVal)
        UserHandler.dropUser('user1')

    def testEditUser(self):
        criteria = {'userName' : 'newUser', 'userID' : 'user1' , 'password' : 'passwd' , 'projects' : []}
        UserHandler.addUser(criteria)
        returnVal, userExists = UserHandler.findUser({'userID' : "user1"}, {'userID' : 1 , '_id' : 0})
        self.assertEqual({'userID' : 'user1'},returnVal)

        UserHandler.editUser({'userID' : 'user1'}, {'userName' : 'updatedUser'})

        updatedReturnVal, _err = UserHandler.findUser({'userID' : 'user1'}, {'userName' : 1, '_id' : 0})
        self.assertEqual({'userName' : 'updatedUser'}, updatedReturnVal)
        UserHandler.dropUser('user1')



        


if __name__ == '__main__':
    unittest.main()

