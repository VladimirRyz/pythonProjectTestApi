import configuration
import requests
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user():
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    body = data.user_body
    headers = data.headers
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(url, json = body, headers=headers)
def post_new_client_kit(authToken, name):
    url=configuration.URL_SERVICE + configuration.CREATE_MAIN_KITS
    body = {
        "name": name
    }
    new_headers = data.headers.copy()
    new_headers['Authorization']=f'Bearer + {authToken}'
    # post запрос на создание нового набора с аргументами  в виде токена и наименования набора
    # url запрос
    # body тело запроса с переменной name которую буду задавать в тестах
    # new_headers заголовок, сначала копируем из data, потом устанавливаем авторизацию
    # форматирую приставку Bearer из требований и полученный при создании пользователя токен
    return requests.post(url, json=body, headers=new_headers)