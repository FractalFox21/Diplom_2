import allure

from data.constants import AUTH_USER_DATA, INVALID_AUTH_DATA
from data.queries import Queries


class TestAuth:

    @allure.title('Позитивный тест авторизации пользователя.')
    def test_auth_user_code_200():
        response =  Queries.post_auth_user(data=AUTH_USER_DATA)
        data = response.json()
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["success"] is True, "Поле 'success' не соответствует ожидаемому,ожидалось True"


    @allure.title('Негативный тест авторизации пользователя, неверные логин и пароль.')
    def test_auth_invalid_data_user_code_401():
        response =  Queries.post_auth_user(data=INVALID_AUTH_DATA)
        data = response.json()
        assert response.status_code == 401, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 401."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"

