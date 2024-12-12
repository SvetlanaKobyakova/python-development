

import requests
import json

from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError



def get_html(url: str) -> str|None:
    try:
        response = requests.get(url)
        status = response.status_code
        # Если НЕ успешный запрос и НЕ переадресация - то ОШИБКА
        if status != 200 and str(status)[0] != 3:
            print(f'Ошибка запроса. Код ответа - {status}')
            return None
        print(f'Код ответа - {status}')
        html = response.text
        return html
    except ConnectionError as error:
        print('Нет ответа от сервера')
        print(error)
        return None
    # print(html)
    # with open('index.html', 'w') as file:
    #     file.write(html)

def parse_html(html: str) -> dict:
    courses = {}
    soup: Bs = Bs(html, 'html.parser')
    current_date = soup.find('h2', class_='h2 blue').text.split('\n')[-1].strip().split()[0]
    table = soup.find('div', class_="module-tableSort")
    rows = table.find_all('tr')[2:]
    courses[current_date] = {}

    for row in rows:
        if not row.find('td', class_='t-center'):
            continue
        code = row.find('td', class_='t-center').text
        number_code = code.split()[0]
        txt_code = code.split()[1]

        name = row.find('td', class_='t-left').text.split('\n')[0]
        value = row.find('td', class_='t-right').text.strip()
        print(f'{number_code} - {txt_code} {name} {value}')

        courses[current_date][txt_code] = {
            'number_code': number_code,
            'name': name,
            'value': value
        }
    return courses

def write_data_to_json(data: dict) -> None:
    with open('courses.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_data_from_json(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# URL = "https://www.alta.ru/currency/"
# html = get_html(URL)
# if html:
#     courses = parse_html(html)
#     write_data_to_json(data=courses)

courses_from_file = get_data_from_json('courses.json')
print(courses_from_file)