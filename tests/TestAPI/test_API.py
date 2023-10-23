import json
import unittest
import requests
import json

class test_API(unittest.TestCase):
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
            response = requests.post(url, data=json_data, headers=headers)
            # Check the response
            self.assertEqual(response.status_code,200,customMsg)
            if response.status_code == 200:
                print('Request was successful.')
                response_data = response.json()
                print('Response:', response_data)
            else:
                print(f'Request failed with status code: {response.status_code}')
                print('Response content:', response.text)


            # If the request was successful, process the response
            if response.status_code == 200:
                # Do something with the response content
                print(response.text)
            else:
                # Handle other HTTP status codes
                print(f"HTTP Status Code: {response.status_code}")

        except requests.exceptions.ConnectionError as e:
            # Handle connection issues
            #self.fail(f"Connection Error: {e}")
            self.fail("Check that API is running locally before running test")
        except requests.exceptions.RequestException as e:
            # Handle other request-related exceptions
            self.fail(f"Request Exception: {e}")
        except Exception as e:
            # Handle other unexpected exceptions
            self.fail(f"An unexpected error occurred: {e}")



if __name__ == '__main__':
    unittest.main()