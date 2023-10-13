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
UserHandler.addUser("John", "John1", "Mejia", ["Numpy Ninjas", "Team"])





class testUserHandler(unittest.TestCase):
    def testAddAndDropUser(self):
        UserHandler.addUser("newUser2", "userLogin", "passwd", ["Numpy Ninjas", "Team"])
        returnVal, isUser = UserHandler.findUser({'userID' : "userLogin"}, {'userID' : 1 , '_id' : 0})
        self.assertEqual({'userID' : 'userLogin'},returnVal)
        UserHandler.dropUser('userLogin')

    # def testEditUser(self):
    #     UserHandler.addUser("newUser2", "userLogin", "passwd", ["Numpy Ninjas", "Team"])
    #     UserHandler.dropUser('userLogin')

        


if __name__ == '__main__':
    unittest.main()

