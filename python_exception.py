import requests

# обработка исключений
"""
try:
    блок,
     где возможна ошибка
except:
    действие,
     в случае ошибки
finally:
    блок кода,
     который выполнится в любом случае
"""
#
# age = input('Enter the age: ')
# try:
#     if age < 18:
#         print('Error')
#     else:
#         print('Ok')
# except:
#     if age.isdigit():
#         if int(age) <18:
#             print('Error')
#         else:
#             print('Ok')
#     else:
#         print('не число')

#
# def send_data():
#     data = {'name': 'Alex', 'age': 26}
#     data = None
#     return Exception('ERROR')
#
# def get_data_from_server():
#     try:
#         data =send_data()
#         print(data)
#     except:
#         data = []
#         for i in data:
#             print(i)
#
# get_data_from_server()

# try:
#     mydict = {'name': 'Dima'}
#     if not mydict.get('age'):
#         print(mydict.get('age'))
#         raise Exception('Такого ключа нет')
# except Exception as err:
#     print(err)


# def check_age(age):
#     if age > 102:
#         raise Exception('Возвраст слишком большой')
#     return age
#
# try:
#     print(check_age(226))
# except:
#     print('Возникла ошибка')

# HTPP
def get_page(url):
    try:
        response =  requests.get(url)
        print(response.status_code)
        print(response.text)
    except:
        print('error')

url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
get_page(url)