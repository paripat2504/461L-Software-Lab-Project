import Handlers.UserHandler as UserHandler
import Database_Constants
import unittest
import pymongo

# Replace these with your MongoDB connection details

mongo = Database_Constants.InitializeGlobals()
mongo_url = mongo.getMongoURL()  # Default MongoDB connection URL
users = mongo.getUsers()
UserHandler.addUser("newUser4", "userLogin1", "passwd", ["Numpy Ninjas", "Team"])



class TestAddUser(unittest.TestCase):
    def testAddUser(self):
        UserHandler.addUser("newUser2", "userLogin", "passwd", ["Numpy Ninjas", "Team"])
        val = UserHandler.findUser({'userID' : "userLogin"}, {'password' : 1 , '_id' : 0})
        self.assertEqual({'password' : 'passwd'},val)
        UserHandler.dropUser('userLogin')


if __name__ == '__main__':
    unittest.main()

