# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

def get_token():
    sender_stand_request.post_new_user()
    res = sender_stand_request.post_new_user()
    if res.ok:
        return res.json()['authToken']
    else:
        return ' '



def positive_assert(name):
    authToken = get_token()
    res = sender_stand_request.post_new_client_kit(authToken, name)
    assert res.status_code == 201
    str_name = res.json()['name']
    assert str_name == name


def negative_assert(name):
    authToken = get_token()
    res = sender_stand_request.post_new_client_kit(authToken, name)
    assert res.status_code == 400

def test_1():
     positive_assert('a')

def test_2():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_3():
    negative_assert('')


def test_4():
    negative_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')


def test_5():
    positive_assert('QWErty')

def test_6():
    positive_assert('Мария')


def test_7():
    positive_assert('"№%@",')


def test_8():
    positive_assert('Человек и КО')


def test_9():
    positive_assert('123')


def test_10():
    negative_assert()


def test_11():
    negative_assert(123)


