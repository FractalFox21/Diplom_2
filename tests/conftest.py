import pytest
import requests

from data.generator import GenerateUsers
from data.handles import BASE_URL, URL_USER
from data.queries import Queries



#фикстура для создания и удаления временного пользователя
@pytest.fixture(scope='function')
def create_and_delete_user():
    user = GenerateUsers.generate_fake_user()
    response = Queries.post_create_user(data=user)
    token = response.json()['accessToken']
    yield user , token , response
    requests.delete(f'{BASE_URL}{URL_USER}', headers={'Authorization': f'{token}'})
