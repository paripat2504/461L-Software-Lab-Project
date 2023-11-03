# Import necessary modules
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
#from databasescript import Database  # Import the Database class


from Database.Handlers.UserHandler import UserHandler as uH
from Database.Handlers.ProjectsHandler import ProjectHandler as projH
 
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

        validLogin = userHandler.validateUser({"userID":userID, "password":password})
        # Call the login function from the Database class

        if validLogin == True:
            return jsonify({'message': 'Login successful'})
        
        else:
            return jsonify({'message': 'Invalid credentials'})
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

        validLogin = userHandler.addUser({"userName":username, "userID":userID, "password":password})
        if validLogin == False:
            return jsonify({'message': 'Username has already been taken'})
        else:
            return jsonify({'message': 'User registered successfully'})
    else:
        return jsonify({'message': 'Invalid request'})
# Define project Creation endpoint and logic
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
    
# Run the Flask application
if __name__ == '__main__':
    userHandler = uH(True)
    app.run(debug=True)
    userHandler.dropUserCollection()
