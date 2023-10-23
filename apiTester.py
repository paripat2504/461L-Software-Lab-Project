

import requests
import json

# Define the URL of the Flask API endpoint
url = 'http://localhost:5000/api/signup'  # Replace with the actual URL

# Define the JSON data you want to send
data = {
    'userName': 'Numpy_Ninja',
    'userID' : 'ninja420',
    'password': 'morningstar'
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Set the headers to indicate JSON content
headers = {'Content-Type': 'application/json'}

# Make a POST request with the JSON data
response = requests.post(url, data=json_data, headers=headers)

# Check the response
if response.status_code == 200:
    print('Request was successful.')
    response_data = response.json()
    print('Response:', response_data)
else:
    print(f'Request failed with status code: {response.status_code}')
    print('Response content:', response.text)