# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
import sender_stand_request

headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания новой записи пользователя в системе
# содержат имя, телефон и адрес пользователя
user_body = {
    "firstName": "Анатолий",  # Имя пользователя
    "phone": "+79995553322",  # Контактный телефон пользователя
    "address": "г. Москва, ул. Пушкина, д. 10"  # Адрес пользователя
}


#Authorization = {
#   "Authorization": "Bearer " + "sender_stand_request.auth_token"
#}

#kit_body = {
#    "name": "Мой набор"
#}