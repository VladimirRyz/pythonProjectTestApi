# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request
# Функция для проверки получения токена при создании нового пользователя
def get_token():
    sender_stand_request.post_new_user()
    res = sender_stand_request.post_new_user()
    if res.ok:
        return res.json()['authToken']
    else:
        return ' '
# Сравниваю переменную res на наличия в ней токена

#Функция позитивных проверок
def positive_assert(name):
    authToken = get_token()
    res = sender_stand_request.post_new_client_kit(authToken, name)
    assert res.status_code == 201
    str_name = res.json()['name']
    assert str_name == name
# Проверяю код ответа и соответствие в ответе поля name отправленному
# Функция негативных проверок
def negative_assert(name):
    authToken = get_token()
    res = sender_stand_request.post_new_client_kit(authToken, name)
    assert res.status_code == 400
# Тесты по номерам в соответствии с чек-листом

def test_one_leter_in_name_get_success_response():
     positive_assert('a')

def test_511_leter_in_name_get_success_response():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_null_leter_in_name_get_success_response():
    negative_assert('')


def test_512_leter_in_name_get_success_response():
    negative_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')


def test_english_leter_in_name_get_success_response():
    positive_assert('QWErty')

def test_russian_leter_in_name_get_success_response():
    positive_assert('Мария')


def test_special_characters_leter_in_name_get_success_response():
    positive_assert('"№%@",')


def test_spaces_allowed_leter_in_name_get_success_response():
    positive_assert('Человек и КО')


def test_numbers_allowed_leter_in_name_get_success_response():
    positive_assert('123')

#Функция негативной проверки на отсутвие обязательного параметра
def negative_assert_no_first_name(name):
    authToken = get_token()
    res = sender_stand_request.post_new_client_kit(authToken,name)
    assert res.status_code == 400
    assert res.json()["message"] == "Не все необходимые параметры были переданы"
def test_parameter_not_passed_in_request():
    negative_assert_no_first_name(None)


def test_a_different_parameter_type_number_was_passed():
    negative_assert(123)