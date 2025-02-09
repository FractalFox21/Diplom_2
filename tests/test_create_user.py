import allure

from data.constants import invalid_data_user, test_user_data
from data.generator import generate_fake_user
from data.queries import Queries





@allure.title('Позитивный тест создания нового пользователя с уникальными данными.')
def test_create_new_unique_user_code_200():
    fake_user = generate_fake_user()
    response = Queries.post_create_user(data=fake_user)

    assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
    data = response.json()
    assert data["success"] is True, "Поле 'success' не соответствует ожидаемому,ожидалось True"


@allure.title('негативный тест создания пользователя.')
def test_create_non_unique_user_code_403():
    response = Queries.post_create_user(data=test_user_data)
    assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
    data = response.json()
    assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"

@allure.title('негативный тест создания нового пользователя, не указан пароль')
def test_create_user_without_pass_401():
    response = Queries.post_create_user(data=invalid_data_user)

    assert response.status_code == 403, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 403."
    data = response.json()
    assert data["success"] is False, "Поле 'success' не соответствует ожидаемому,ожидалось False"