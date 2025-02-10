import pytest
import requests

from data.constants import EDIT_BACK_USER_DATA
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
    def patch_redact_data(data=None, token=None):
        url = f"{BASE_URL}{URL_USER}"
        response = requests.patch(url, json=data,  headers={'Authorization': f'{token}'})
        return response


    @staticmethod
    def delete_user(data=None, token=None):
        url = f"{BASE_URL}{URL_USER}"
        requests.patch(url, json=data,  headers={'Authorization': f'{token}'})

