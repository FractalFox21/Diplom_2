import allure
import requests

from data.constants import AUTH_USER_DATA, REDACT_USER_DATA, EDIT_BACK_USER_DATA
from data.generator import GenerateUsers
from data.handles import BASE_URL, URL_USER
from data.queries import Queries


class TestRedact:

    @allure.title('Позитивный тест редактирования данных пользователя.')
    def test_redact_user_name_code_200(self):
        user = GenerateUsers.generate_fake_user()
        auth =  Queries.post_create_user(data=user)
        token = auth.json()['accessToken']
        user["name"] = GenerateUsers.generate_fake_name()
        response = Queries.patch_redact_data(data=user, token=token)
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."

    def test_redact_user_email_code_200(self):
        user = GenerateUsers.generate_fake_user()
        auth =  Queries.post_create_user(data=user)
        token = auth.json()['accessToken']
        user["email"] = GenerateUsers.generate_fake_email()
        response = Queries.patch_redact_data(data=user, token=token)
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."


    @allure.title('Позитивный тест редактирования данных пользователя.')
    def test_redact_user_name_no_token_code_401(self):
        user = GenerateUsers.generate_fake_email_name()
        response = Queries.patch_redact_data(data=user)
        data = response.json()
        assert response.status_code == 401, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось True"

    @allure.title('Позитивный тест редактирования данных пользователя.')
    def test_redact_user_email_no_token_code_401(self):
        user = GenerateUsers.generate_fake_email_name()
        response = Queries.patch_redact_data(data=user)
        data = response.json()
        assert response.status_code == 401, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось True"

