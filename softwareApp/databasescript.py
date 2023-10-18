import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Database.Handlers import UserHandler

UHandler = UserHandler.UserHandler(False)
class Database:

    def __init__(self):
        self.userIDDatabase = []
        self.passwordDatabase = []
    #SignUp: 1 = successful signup, 0 = unsuccessful
    def signup(self, username, userID, password):
        criteria = {'userName' : username, 'userID' : userID, 'password' : password }
        valuesToReturn = None
        returnValue, doesUserExist = UHandler.findUser(criteria, valuesToReturn)
        if doesUserExist == True:
            #there is a user in the database
            return False
        else:
            crit_with_team = {'userName' : criteria.get('userName'), 'userID' : criteria.get('userID'), 'password' : criteria.get('password'), 'projects' : []}
            UHandler.addUser(crit_with_team)
            returnValue, doesUserExist = UHandler.findUser(criteria, valuesToReturn)
            print("Welcome ", crit_with_team.get('userName'), "! You have been added!")

            if doesUserExist == False:
                return True
            else:
                return False
    #Login: 1 = successful login, 0 = unsuccessful
    def login(self, username, userID, password):
        criteria = {'userName' : username, 'userID' : userID, 'password' : password }
        valuesToReturn = None
        returnValue, doesUserExist = UHandler.findUser(criteria, valuesToReturn)
        if doesUserExist == True:
            #the login matches user in database
            return True
        else:
            return False

        
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
        userID =   input("EnterUserID: ")
        passWord = input("Enter Password: ")
        print(db.signup(userName, userID, passWord))
    elif(signup_or_login == "2"):
        userName = input("Enter Username: ")
        userID =   input("EnterUserID: ")
        passWord = input("Enter Password: ")
        print(db.login(userName, userID, passWord))
    else:
        print("Invalid Response")