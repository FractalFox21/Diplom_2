import allure
from data.generator import GenerateUsers
from data.queries import Queries


class TestRedact:

    @allure.title('Позитивный тест редактирования данных пользователя.')
    def test_redact_user_name_code_200(self, create_and_delete_user):
        user = create_and_delete_user
        new_name  = GenerateUsers.generate_fake_name()
        user[0]["name"] = new_name
        response = Queries.patch_redact_data(data=user[0], token=user[1])
        data = response.json()
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["user"]["name"] == new_name, f"Поле 'name' не соответствует ожидаемому,ожидалось {new_name}"

    @allure.title('Позитивный тест редактирования данных пользователя.')
    def test_redact_user_email_code_200(self, create_and_delete_user):
        user = create_and_delete_user
        new_email  = GenerateUsers.generate_fake_email()
        user[0]["email"] = new_email
        response = Queries.patch_redact_data(data=user[0], token=user[1])
        data = response.json()
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["user"]["email"] == new_email, f"Поле 'name' не соответствует ожидаемому,ожидалось {new_email}"


    @allure.title('Позитивный тест редактирования данных пользователя.')
    def test_redact_user_name_no_token_code_401(self, create_and_delete_user):
        user = create_and_delete_user
        new_name = GenerateUsers.generate_fake_name()
        user[0]["name"] = new_name
        response = Queries.patch_redact_data(data=user[0])
        data = response.json()
        assert response.status_code == 401, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось True"

    @allure.title('Позитивный тест редактирования данных пользователя.')
    def test_redact_user_email_no_token_code_401(self, create_and_delete_user):
        user = create_and_delete_user
        new_email  = GenerateUsers.generate_fake_email()
        user[0]["email"] = new_email
        response = Queries.patch_redact_data(data=user[0])
        data = response.json()
        assert response.status_code == 401, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось True"
