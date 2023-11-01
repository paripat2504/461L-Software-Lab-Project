
import json
import requests

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../API/')))
import api

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Database/Handlers/')))
import UserHandler

from flask import Flask
from flask_testing import TestCase

uH = UserHandler.UserHandler(True)
uH.resetUserCollection()

class test_API(TestCase):

    def create_app(self):
        return api.app
            
    

    def test_APIAddUser(self):
        customMsg = "Succeeded!"
        # Define the URL of the Flask API endpoint
        url = 'http://localhost:5000/signup'  # Replace with the actual URL


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
        try:    
            response = self.client.post(url, data=json_data, headers=headers)
            # Check the response
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.json['message'],'User successfully created')

        except requests.exceptions.RequestException as e:
            # Handle other request-related exceptions
            self.fail(f"Request Exception: {e}")
        except Exception as e:
            # Handle other unexpected exceptions
            self.fail(f"An unexpected error occurred: {e}")

        
        uH.resetUserCollection()

    def test_APIAddUserButUserNameExists(self):
        customMsg = "Succeeded!"
        # Define the URL of the Flask API endpoint
        url = 'http://localhost:5000/signup'  # Replace with the actual URL


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
        try:    
            response = self.client.post(url, data=json_data, headers=headers)
            # Check the response
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.json['message'],'User successfully created')
            response = self.client.post(url, data=json_data, headers=headers)
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.json['message'],'User already exists with that username or userID')


        except requests.exceptions.RequestException as e:
            # Handle other request-related exceptions
            self.fail(f"Request Exception: {e}")
        except Exception as e:
            # Handle other unexpected exceptions
            self.fail(f"An unexpected error occurred: {e}")

        
        uH.resetUserCollection()

    def test_Login(self):

        url = 'http://localhost:5000/signup'  # Replace with the actual URL


        data = {
            'userName': 'Numpy_Ninja',
            'userID' : 'ninja420',
            'password': 'morningstar'
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(url, data=json_data, headers=headers)




        url = 'http://localhost:5000/login'  # Replace with the actual URL
        # Define the JSON data you want to send
        data = {
            'userID' : 'ninja420',
            'password': 'morningstar'
        }

        # Convert the data to JSON format
        json_data = json.dumps(data)

        # Set the headers to indicate JSON content
        headers = {'Content-Type': 'application/json'}

        # Make a POST request with the JSON data
        try:    
            response = self.client.post(url, data=json_data, headers=headers)
            # Check the response
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.json['message'],'Login successful')

        except Exception as e:
            print({e})

        uH.resetUserCollection()
        
            


if __name__ == '__main__':
    import unittest
    unittest.main()