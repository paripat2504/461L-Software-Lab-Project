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

    # def testEditUser(self):
    #     UserHandler.addUser("newUser2", "userLogin", "passwd", ["Numpy Ninjas", "Team"])
    #     UserHandler.dropUser('userLogin')

        


if __name__ == '__main__':
    unittest.main()

