import allure

from data.constants import TEST_USER_DATA, INVALID_USER_DATA
from data.queries import Queries


class TestCreateUser:
    @allure.title('Позитивный тест создания нового пользователя с уникальными данными.')
    def test_create_new_unique_user_code_200(self, create_and_delete_user):
        user = create_and_delete_user
        data = user[2].json()
        assert user[2].status_code == 200, f"Статус код: {user[2].status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["success"] is True, "Поле 'success' не соответствует ожидаемому,ожидалось True"


    @allure.title('негативный тест создания пользователя, такой пользователь уже есть.')
    def test_create_non_unique_user_code_403(self):
        response = Queries.post_create_user(data=TEST_USER_DATA)
        data = response.json()
        assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"

    @allure.title('негативный тест создания нового пользователя, не указан пароль')
    def test_create_user_without_pass_401(self):
        response = Queries.post_create_user(data=INVALID_USER_DATA)
        data = response.json()
        assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"

