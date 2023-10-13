
import sys
import os
project_folder = os.path.dirname(os.path.abspath(__file__))
project_folder_parent = os.path.dirname("461L-Software-Lab-Project")
sys.path.append(project_folder_parent)
from Database.Handlers import UserHandler
class Database:

    def __init__(self):
        self.userIDDatabase = []
        self.passwordDatabase = []
    #SignUp: 1 = successful signup, 0 = unsuccessful
    def signup(self, username, userID, password):
        criteria = {'userName' : username, 'userID' : userID, 'password' : password }
        valuesToReturn = None
        returnValue, doesUserExist = UserHandler.findUser(criteria, valuesToReturn)
        if doesUserExist:
            #there is a user in the database
            return False
        else:
            UserHandler.addUser(criteria, valuesToReturn)
            if UserHandler.findUser == 1:
                return True
            else:
                return False
    #Login: 1 = successful login, 0 = unsuccessful
    def login(self, username, userID, password):
        criteria = {'userName' : username, 'userID' : userID, 'password' : password }
        valuesToReturn = None
        returnValue, doesUserExist = UserHandler.findUser(criteria, valuesToReturn)
        if doesUserExist:
            #the login matches user in database
            return True
        else:
            return False
    
    
    # def signup(self, userName, passWord):
    #     if self.__checkUserInDatabase(userName) == 1:
    #         print("UserName has already been taken")
    #         return 0
    #     self.userIDDatabase.append(userName)
    #     self.passwordDatabase.append(passWord)
    #     print("User has ben registered and added to the database")

    # def login(self, userName, passWord):
    #     if userName in self.userIDDatabase:
    #         #Check if the passord matches
    #         user_index = self.userIDDatabase.index(userName)
    #         if self.passwordDatabase[user_index] == passWord:
    #             print(userName + "logged in")
    #         else:
    #             print("Incorrect Password")
    #     else:
    #         print("User not found")
        
    def __checkUserInDatabase(self, userName):
        if userName in self.userIDDatabase:
            return 1
        else:
            return 0
        
        
db = Database()



while(1):
    
    signup_or_login = input("Sign up (1) or login (2)")

    if(signup_or_login == "1"):
        userName = input("Enter Username: ")
        userID =   input("EnterUserID")
        passWord = input("Enter Password: ")
        print(db.signup(userName, userID, passWord))
    else:
        userName = input("Enter Username: ")
        userID =   input("EnterUserID")
        passWord = input("Enter Password: ")
        print(db.login(userName, userID, passWord))