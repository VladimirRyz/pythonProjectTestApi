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

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
#response = post_new_user(data.user_body);

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
#print(response.status_code)
#print(response.json())
#authToken = response.json().get('authToken')
#response.json())

#Сохраняю полученный в ответе токен в переменную
def post_new_client_kit(authToken, name):
    url=configuration.URL_SERVICE + configuration.CREATE_MAIN_KITS
    body = {
        "name": name
    }
    new_headers = data.headers.copy()
    new_headers['Authorization']=f'Bearer + {authToken}'
    # post запрос на создание нового набора
    return requests.post(url, json=body, headers=new_headers)
# Вызов функции post_new_client_kit с телом запроса для создание нового набора из модуля data
#response = post_new_client_kit();