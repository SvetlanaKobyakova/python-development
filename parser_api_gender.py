

import requests


def get_gender_data(name: str) -> dict:
    params = {
        "name": name
    }
    url = "https://api.genderize.io/"
    #  или url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

def parse_gender_data(data: dict) -> None:
    pass

"""
Дан список имен: Елена, Владимир, 345454 Саша, рпакпвроп
Создать файл names.txt, содержащий для каждого имени следующую информацию:
Имя - вова
Пол - мужской
Вероятность - 99%

Имя - рпрарпао
Пол - не определен
Вероятность - не определена
Некорректное имя!

"""


gender_data = get_gender_data(name="Елена")
print(parse_gender_data(data=gender_data))

