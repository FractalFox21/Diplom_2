import allure

from data.constants import AUTH_USER_DATA, NO_ACСESS
from data.queries import Queries

@allure.suite('Получение заказов конкретного пользователя.')
class TestCheckOrder:

    @allure.title('Позитивный тест проверки заказов пользователя.')
    @allure.description('Авторизуем пользователя и отправляем запрос на список заказов с его токеном.\
    Ожидаемый статус код 200.\
    Ожидаемый ответ запроса содержит "orders".')

    def test_auth_user_back_info_code_200(self):
        auth = Queries.post_auth_user(data=AUTH_USER_DATA)
        token = auth.json()['accessToken']
        response = Queries.get_check_order(token=token)
        data = response.json()
        assert response.status_code == 200, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 200."
        assert "orders" in data, f"Ответ {data} не содержит 'orders'."

    @allure.title('Негативный тест проверки заказов пользователя, не указан токен.')
    @allure.description('Отправляем запрос на список заказов без токена.\
    Ожидаемый статус код 401.')
    def test_check_orders_no_token_code_401(self):
        response = Queries.get_check_order()
        data = response.json()
        assert response.status_code == 401, f"Статус код: {response.status_code} не соответствует ожидаемому, ожидалось 401."
        assert data["message"] == NO_ACСESS , f"Сообщение об ошибке: {data["message"]} не соответствует ожидаемому, ожидалось {NO_ACСESS}."

