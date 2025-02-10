import requests

from data.handles import BASE_URL, URL_REGISTER, URL_AUTH, URL_USER


class Queries:

    @staticmethod
    def post_create_user(data=None):
        url = f"{BASE_URL}{URL_REGISTER}"
        response = requests.post(url, json=data)
        return response


    @staticmethod
    def post_auth_user(data=None):
        url = f"{BASE_URL}{URL_AUTH}"
        response = requests.post(url, json=data)
        return response

    @staticmethod
    def post_redact_data(data=None, token=None):
        url = f"{BASE_URL}{URL_USER}"
        response = requests.post(url, data=data, headers={'Authorization': token})
        return response