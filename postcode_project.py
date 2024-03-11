import json

import requests


class PostCodes:
    def __init__(self):
        self.link = "https://postcodes.io/"

    def get_random_postcode(self):
        endpoint = "random/postcodes"
        response = requests.get(f"{self.link}{endpoint}")
        data = response.json()
        postcode = data['result']['postcode']
        return postcode

    def validate_postcode(self, postcode):
        endpoint = f"/postcodes/{postcode}/validate"
        response = requests.get(f"{self.link}{endpoint}")
        data = response.json()
        validate_information = data['result']
        return validate_information

    def find_nearest_postcode(self, postcode):
        endpoint = f"/postcodes/{postcode}/nearest"
        response = requests.get(f"{self.link}{endpoint}")
        data = response.json()
        nearest_information = data['result']
        return nearest_information

    def query_for_postcode(self, postcode):
        endpoint = f"/postcodes?q={postcode}"
        response = requests.get(f"{self.link}{endpoint}")
        data = response.json()
        query_information = data['result']
        return query_information

    def terminated_postcode(self, postcode):
        endpoint = f"terminated_postcodes/{postcode}"
        response = requests.get(f"{self.link}{endpoint}")
        data = response.json()
        terminated_information = data['status']
        return terminated_information

objOne=PostCodes()
# print(objOne.get_random_postcode())
# print(objOne.validate_postcode('M25 3HW'))
# print(objOne.find_nearest_postcode('M25 3HW'))
# print(objOne.query_for_postcode('M25 3HW'))
print(objOne.terminated_postcode('M25 3ed'))