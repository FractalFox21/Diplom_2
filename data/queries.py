import requests

from data.constants import auth_test_user, test_user_data
from data.handles import BASE_URL, URL_REGISTER, URL_AUTH


class Queries:

    @staticmethod
    def post_create_user(data=None):
        url = f"{BASE_URL}{URL_REGISTER}"
        response = requests.post(url, json=data)
        return response


    @staticmethod
    def post_auth_test_user():
        url = f"{BASE_URL}{URL_AUTH}"
        response = requests.post(url, json=auth_test_user)
        return response

