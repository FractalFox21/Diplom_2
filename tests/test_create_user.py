import allure

from data.constants import TEST_USER_DATA
from data.queries import Queries

@allure.suite('Создание пользователя.')
class TestCreateUser:
    @allure.title('Позитивный тест создания нового пользователя с уникальными данными.')
    @allure.description('Создаем нового пользователя с валидными данными.\
    Ожидаемый статус код 200.\
    Ожидаемый ответ запроса содержит "success" is True.')
    def test_create_new_unique_user_code_200(self, create_and_delete_user):
        user = create_and_delete_user
        data = user[2].json()
        assert user[2].status_code == 200, f"Статус код: {user[2].status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["success"] is True, "Поле 'success' не соответствует ожидаемому,ожидалось True"

    @allure.title('Негативный тест создания пользователя, такой пользователь уже есть.')
    @allure.description('Отправляем запрос на создание пользователя указанием логина, который уже есть в базе.\
    Ожидаемый статус код 403.\
    Ожидаемый ответ запроса содержит "success" is False.')
    def test_create_non_unique_user_code_403(self):
        response = Queries.post_create_user(data=TEST_USER_DATA)
        data = response.json()
        assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"

    @allure.title('Негативный тест создания нового пользователя, не указан email.')
    @allure.description('Отправляем запрос на создание пользователя без указания логина.\
    Ожидаемый статус код 403.\
    Ожидаемый ответ запроса содержит "success" is False.')
    def test_create_user_without_email_code_401(self, generating_user_data_no_email=None):
        response = Queries.post_create_user(data=generating_user_data_no_email)
        data = response.json()
        assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"

    @allure.title('Негативный тест создания нового пользователя, не указан пароль.')
    @allure.description('Отправляем запрос на создание пользователя без указания пароля.\
    Ожидаемый статус код 403.\
    Ожидаемый ответ запроса содержит "success" is False.')
    def test_create_user_without_pass_code_401(self, generating_user_data_no_pass=None):
        response = Queries.post_create_user(data=generating_user_data_no_pass)
        data = response.json()
        assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"

    @allure.title('негативный тест создания нового пользователя, не указано имя')
    @allure.description('Отправляем запрос на создание пользователя без указания имени.\
    Ожидаемый статус код 403.\
    Ожидаемый ответ запроса содержит "success" is False.')
    def test_create_user_without_name_code_401(self, generating_user_data_no_name=None):
        response = Queries.post_create_user(data=generating_user_data_no_name)
        data = response.json()
        assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"
