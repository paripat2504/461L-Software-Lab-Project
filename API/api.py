# Import necessary modules
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

#import UserHandler
#from databasescript import Database  # Import the Database class
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Database/Handlers/')))


from UserHandler import UserHandler as uH
from ProjectsHandler import ProjectHandler as projH

userHandler = uH(True)
projHandler = projH(True)

# Create the Flask application
app = Flask(__name__)
CORS(app)

# Create an instance of the Database class

# Define login endpoint and logic
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    userID = data.get('userID')
    password = data.get('password')
    
    if userID and password:
        #include username, get username from database
        validLogin, _err = userHandler.validateUser({"userID":userID, "password":password})
        # Call the login function from the Database class
        
        if validLogin == True:
            uDict, err = userHandler.findUser({'userID':userID} ,{'userName':1})
            retrievedUName = uDict['userName']
            return jsonify({'message': 'Login successful', 'userName' : retrievedUName})
        
        else:
            return jsonify({'message': _err})
    else:
        return jsonify({'message': 'Invalid request'})

# Define signup endpoint and logic
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('userName')
    userID = data.get('userID')
    password = data.get('password')
    
    if username and password and userID:
        # Call the signup function from the Database class

        validLogin, _err = userHandler.addUser({"userName":username, "userID":userID, "password":password})
        if validLogin == False:
            return jsonify({'message': _err})
        else:
            return jsonify({'message': 'User successfully created'})
    else:
        return jsonify({'message': 'Invalid request'})




# Define project endpoint and logic
@app.route('/project', methods=['POST'])
def project():
    data = request.get_json()
    userName = data.get('userName')
    projectName = data.get('projectName')
    projectDescription = data.get('projectDescription')
    projectID = data.get('projectID')
    
    if userName and projectName and projectDescription and projectID:
        
        projCreated, _err = projHandler.createProject({"userName":userName, "projectName":projectName, "projectDescription":projectDescription, "projectID":projectID, })
        # Call the login function from the Database class
        
        if projCreated == True:
            return jsonify({'message': 'Project Created successfully'})
        
        else:
            return jsonify({'message': _err})
    else:
        return jsonify({'message': 'Invalid request'})
    
# Define project endpoint and logic for joiningProject
@app.route('/projectJoin', methods=['POST'])
def projectJoin():
    data = request.get_json()
    userName = data.get('userName')
    projectID = data.get('projectID')
    
    if userName and projectID:
        
        projJoined, _err = projHandler.joinProject({"userName":userName, "projectID":projectID})
        
        if projJoined == True:
            return jsonify({'message': 'Project Joined successfully'})
        
        else:
            return jsonify({'message': _err})
    else:
        return jsonify({'message': 'Invalid request'})
    
@app.route('/displayProjects', methods=['POST'])
def displayProjects():
    data = request.get_json()
    userName = data.get('userName')
    
    if userName:
        
        projectsRetreived, _err = projHandler.returnUserProjects(userName)
        if _err == None:
            return jsonify({'message': 'Project Retrieved successfully', 'projects': projectsRetreived})
        else:
            return jsonify({'message': _err})
    else:
        return jsonify({'message': 'Invalid request', 'projects': projectsRetreived})
    

@app.route('/checkInHWSet/', methods=['POST'])
def checkInHWSet():
    data = request.get_json()
    projHandler.checkInHardwareSet({'projectID':data['projectID'],'hwSetID':data['hwSetID'],'amountRequested':data['amountRequested']})
    err = None
    if err != None:
        return jsonify({'message': "Successfully Checked in " + data['amountRequested'] + " " + data['hwSetID']})
    else:
        return jsonify({'message':err})

@app.route('/checkOutHWSet/', methods=['POST'])
def checkOutHWSet():
    data = request.get_json()
    projHandler.checkOutHardwareSet({'projectID':data['projectID'],'hwSetID':data['hwSetID'],'amountRequested':data['amountRequested']})
    err = None
    if err != None:
        return jsonify({'message': "Successfully Checked out " + data['amountRequested'] + " " + data['hwSetID']})
    else:
        return jsonify({'message':err})

@app.route('/displayHardware', methods=['POST'])
def displayHardware():
    HWSet1Availability, HWSet2Availability, HWSet1Capacity, HWSet2Capacity, _err = projHandler.displayHardware()
    hw_dict = {'HWSet1Availability':HWSet1Availability, 'HWSet2Availability':HWSet2Availability, 'HWSet1Capacity':HWSet1Capacity, 'HWSet2Capacity':HWSet2Capacity}
    if _err == True:
        return jsonify({'message':'Sucessfully Gathered Avaiabilities and Capacities', 'hw_dict':hw_dict})
    else:
        return jsonify({'message' : "HWSet info couldnt be retrieved"})
# Run the Flask application
if __name__ == '__main__':
    
    app.run(debug=True)

