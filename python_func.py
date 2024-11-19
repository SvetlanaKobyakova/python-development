# def hello():
#     print("Hello")
#
# def bye():
#     print("Bye")

# hello()
# bye()

# def print_name(name):
#     print(name)

#  сигнатура фукции - имя и параметры
# def print_info(name, lastname, age, city):
#     info = {
#         'name': name,
#         'last_name': lastname,
#         'age': age,
#         'city':city
#     }
    #return info

# user_name = "Dmitriy"
# user_lastname = "Ivanov"
# user_age = 32
# user_city = "Moskow"

# позиционные аргументы
# print_info(user_name, user_lastname, user_age, user_city)

# именованные аргументы
# print_info(name=user_name, lastname=user_lastname, age=user_age, city=user_city)

# комбинированный способ (именованные аргументы должны следовать за позиционными!!!)
# print_info(user_name, user_lastname, age=user_age, city=user_city)

# result = print_info(name=user_name, lastname=user_lastname, age=user_age, city="Moscow")
# print(result)
# print(print_info(name=user_name, lastname=user_lastname, age=user_age, city="Moscow"))

# def hello(name):
#     print(f"Hello, {name}")
#
# def main():
#     hello('Sasha')


def text_analyse(text):
    """
    :param text='hello':
    :return: {'h':1, 'e':1, 'l':2, 'o':1}
    """
    stat = {}
    for s in text:
        stat[s] = text.count(s)
    return stat

print(text_analyse(text = "hello"))


def text_to_list(text: str) -> list:
    return text.split()

print(text_to_list(text="I love python string"))


emails = [
    "admin@mail.ru",
    "alex@yandex.ru",
    "alena@mail.ru",
    "igor@gmail.ru"
]

def get_emails(in_emails: list[str], domen: str = '.ru') -> list:
    emails = []
    for email in in_emails:
        if email.endswith(domen):
            emails.append(email)

    return emails
print(get_emails(in_emails=emails, domen='@yandex.ru'))


def check_age(age: int|str) -> bool:
    if isinstance(age, int):
        if age < 18:
            return False
        else:
            return True

    if isinstance(age, str):
        if age.isdigit():
            if int(age) < 18:
                return False
            else:
                return True
        else:
            return False

    return False

age = 21
if check_age(age):
    print('OK')
else:
    print('ERROR!!')
