import UserHandler
class Database:

    def __init__(self):
        self.userIDDatabase = []
        self.passwordDatabase = []
    #SignUp: 1 = successful signup, 0 = unsuccessful
    def signup(username, userID, password):
        dataToPass = [username, userID, password]
        if UserHandler.findUser(dataToPass) == 1:
            #there is a user in the database
            return 0
        else:
            UserHandler.addUser(dataToPass)
            if UserHandler.findUser == 1:
                return 1
            else:
                return 0
    #Login: 1 = successful login, 0 = unsuccessful
    def login(username, userID, password):
        dataToPass = [username, userID, password]
        if UserHandler.findUser(dataToPass) == 1:
            #the login matches user in database
            return 1
        else:
            return 0
    
    
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
        passWord = input("Enter Password: ")
        db.signup(userName, passWord)
    else:
        userName = input("Enter Username: ")
        passWord = input("Enter Password: ")
        db.login(userName, passWord)