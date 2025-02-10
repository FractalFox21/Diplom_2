import allure

from data.constants import ORDER, INVALID_ORDER, AUTH_USER_DATA
from data.queries import Queries


class TestCheckOrder:

    @allure.title('Позитивный тест оформления заказа с авторизованным пользователем и ингредиентами')
    def test_auth_user_back_info_code_200(self):
        auth = Queries.post_auth_user(data=AUTH_USER_DATA)
        token = auth.json()['accessToken']
        response = Queries.get_check_order(token=token)
        data = response.json()
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert "orders" in data, f"Ответ {data} не содержит 'orders'."

    @allure.title('Негативный тест оформления заказа с авторизованным пользователем и ингредиентами')
    def test_check_orders_no_token_code_401(self):
        response = Queries.get_check_order()
        assert response.status_code == 401, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 401."

