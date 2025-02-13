import allure

from data.constants import ORDER, INVALID_ORDER, NO_INGREDIENTS, ERROR_TITLE
from data.queries import Queries

@allure.suite('Создание заказа.')
class TestCreateOrder:

    @allure.title('Позитивный тест оформления заказа с авторизованным пользователем и ингредиентами')
    @allure.description('Авторизуем пользователя, отправляем запрос на создание заказа с указанием токена и ингредиентами.\
    Ожидаемый статус код 200.\
    Ожидаемый ответ запроса содержит статус "done".')
    def test_create_order_auth_user_back_data_code_200(self, create_and_delete_user):
            user = create_and_delete_user
            response = Queries.post_create_order(data=ORDER, token=user[1])
            data = response.json()
            assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
            assert data["order"]["status"] == "done", f"Статус заказа: {data["order"]["status"]} не соответствует ожидаемому, ожидалось 'done'."

    @allure.title('Позитивный тест оформления заказа с ингредиентами, но без авторизации')
    @allure.description('Отправляем запрос на создание заказа с ингредиентами, но без токена.\
    Ожидаемый статус код 200.\
    Ожидаемый ответ запроса содержит статус "done".')
    def test_create_order_back_mini_information_code_200(self):
        response = Queries.post_create_order(data=ORDER)
        data = response.json()
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert "status" not in data['order'], f"Ответ {data["order"]} содержит 'status'."

    @allure.title('Негативный тест оформления заказа с авторизованным пользователем, но без ингредиентов')
    @allure.description('Авторизуем пользователя, отправляем запрос на создание заказа с указанием токена, но без ингредиентов.\
    Ожидаемый статус код 400.')
    def test_create_order_auth_user_no_ing_code_400(self, create_and_delete_user):
            user = create_and_delete_user
            response = Queries.post_create_order(token=user[1])
            data = response.json()
            assert response.status_code == 400, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 400."
            assert data["message"] == NO_INGREDIENTS, f"Сообщение об ошибке: {data["message"]} не соответствует ожидаемому, ожидалось {NO_INGREDIENTS}."


    @allure.title('Негативный тест оформления заказа с авторизованным пользователем и неверным хэшем ингредиента')
    @allure.description('Авторизуем пользователя, отправляем запрос на создание заказа с указанием токена и ингредиентами. У одного ингредиента неверный хэш.\
    Ожидаемый статус код 500.')
    def test_create_order_auth_user_bad_hash_code_500(self, create_and_delete_user):
            user = create_and_delete_user
            response = Queries.post_create_order(data=INVALID_ORDER, token=user[1])
            assert response.status_code == 500, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 500."
            assert ERROR_TITLE in response.text, f"В ответе не содержится информация об ошибке, ожидалось {NO_INGREDIENTS}."

