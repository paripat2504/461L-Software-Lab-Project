# Import necessary modules
from re import T
from flask import Flask, request, jsonify
from flask_cors import CORS
#from databasescript import Database  # Import the Database class

from Database.Handlers import UserHandler

# Create the Flask application
app = Flask(__name__)
CORS(app)

# Create an instance of the Database class

# Define login endpoint and logic
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    userID = data.get('userID')
    password = data.get('password')

    dict = {}
    
    if username and password:
        # Call the login function from the Database class
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid request'})

# Define signup endpoint and logic
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        # Call the signup function from the Database class

        result = False
        if result == True:
            return jsonify({'message': 'Username has already been taken'})
        else:
            return jsonify({'message': 'User registered successfully'})
    else:
        return jsonify({'message': 'Invalid request'})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
