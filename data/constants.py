#данные для оформления заказа
ORDER = {"ingredients": [
                 "61c0c5a71d1f82001bdaaa6d",
                 "61c0c5a71d1f82001bdaaa71",
                 "61c0c5a71d1f82001bdaaa72",
                 "61c0c5a71d1f82001bdaaa76"]}

INVALID_ORDER  = {"ingredients": [
                 "61c0c5a71d",
                 "61c0c5a71d1f82001bdaaa76"]}

T_EMAIL = "test_test@mail.ru"
T_PASS = "Test101+"
T_NAME = "Testo Testo"

#данные существуюзего пользователя
AUTH_USER_DATA = {
    "email": T_EMAIL,
    "password": T_PASS}

#данные существующего пользователя с именем
TEST_USER_DATA = {
    "email": T_EMAIL,
    "password": T_PASS,
    "name": T_NAME}

#данные пользователя, которого нет в системе
INVALID_AUTH_DATA = {
    "email": "test0000v@mail.ru",
    "password": "Test10000"}

#данные пользователя без email
INVALID_MAIL_USER_DATA = {
    "email": "",
    "password": T_PASS,
    "name": T_NAME}

#данные пользователя без password
INVALID_EMAIL_USER_DATA = {
    "email": "test0000v@mail.ru",
    "password": "",
    "name": T_NAME}

#данные пользователя без name
INVALID_NAME_USER_DATA = {
    "email": "test0000v@mail.ru",
    "password": T_PASS,
    "name": ""}


