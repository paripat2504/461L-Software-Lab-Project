import json
import random
import string
import sys
import os

import pymongo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from Database.Handlers import UserHandler
import unittest

# Replace these with your MongoDB connection details

UHandler = UserHandler.UserHandler()

def generateUserName(length=8):
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    return username

def dropUserCollection():
    UHandler.resetUserCollection()

class testUserHandler(unittest.TestCase):
    def testAddAndDropUser(self):
        criteria = {'userName' : 'newUser', 'userID' : 'user1' , 'password' : 'passwd' , 'projects' : []}
        UHandler.addUser(criteria)
        UHandler.addUser(criteria)

        returnVal, userExists = UHandler.findUser({'userID' : "user1"}, {'userID' : 1 , '_id' : 0})
        self.assertEqual({'userID' : 'user1'},returnVal)
        dropUserCollection()

    def testEditUser(self):
        criteria = {'userName' : 'newUser', 'userID' : 'user1' , 'password' : 'passwd' , 'projects' : []}
        UHandler.addUser(criteria)
        returnVal, userExists = UHandler.findUser({'userID' : "user1"}, {'userID' : 1 , '_id' : 0})
        self.assertEqual({'userID' : 'user1'},returnVal)

        UHandler.editUser({'userID' : 'user1'}, {'userName' : 'updatedUser'})

        updatedReturnVal, _err = UHandler.findUser({'userID' : 'user1'}, {'userName' : 1, '_id' : 0})
        self.assertEqual({'userName' : 'updatedUser'}, updatedReturnVal)

        dropUserCollection()

    def testDropUser(self):
        criteria = {'userName' : 'newUser', 'userID' : 'user1' , 'password' : 'passwd' , 'projects' : []}
        UHandler.addUser(criteria)
        returnVal, userExists = UHandler.findUser({'userID' : "user1"}, {'userID' : 1 , '_id' : 0})
        self.assertEqual({'userID' : 'user1'},returnVal)
        self.assertEqual(userExists, True)

        UHandler.dropUser('user1')
        returnVal, userExists = UHandler.findUser({'userID' : "user1"}, {'userID' : 1 , '_id' : 0})

        self.assertEqual(None, returnVal)
        self.assertEqual(userExists, False)

        dropUserCollection()



if __name__ == '__main__':
    dropUserCollection()
    unittest.main()

