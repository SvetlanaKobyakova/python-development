import requests
from random import randint


def get_image_link(url:str) -> str:
    resp = requests.get(url)
    data = resp.json()
    link = data.get("message")

    return link

def download_image(url: str) -> None:
    print(url)
    resp = requests.get(url)
    image = resp.content
    with open("image.jpg", "wb") as f:
        f.write(image)




# api_url = "https://dog.ceo/api/breeds/image/random"
# link = get_image_link(url=api_url)
# download_image(url=link)


"""
1. Скачать 30 разных картинок
2. создать папки для каждой породы собак
3. имя картинки должно быть poroda_img_randint.jpg
4*. реализовать проверку существования файла с таким именем
    (если файл с таким именем существует, сгенерировать случайное число еще раз)

api_url = "https://dog.ceo/api/breeds/image/random"
/api/breeds - PATH-param (параметры пути)

"https://api.genderize.io?name=misha"
? - отделяет домен от QUERY- параметров
name=misha - QUERY-param (параметр запроса)
"""

print(randint(1,1000))