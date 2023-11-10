
# import ProjectsHandler

# pH = ProjectsHandler.ProjectHandler(True)
# pH.checkOutHardwareSet({'hwSetID':'Computers','projectID':'John123','amountRequested':20})

import UserHandler

uh = UserHandler.UserHandler(True)

uh.addUser({"userName":"hello","userID":"world","projects":["yoo"],"password":"newPass"})
# y = 4