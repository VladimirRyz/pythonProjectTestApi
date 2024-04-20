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


def test_kit_name():
    authToken = get_token()
    res = sender_stand_request.post_new_client_kit(authToken, 'Dfcy')
    assert res.status_code == 201






