from xml.etree.ElementTree import indent

import requests
import json
from bs4 import BeautifullSoup as Bs

class Parser:
    def __init__(self, url):
        self.url = url
        self.data_weather = {}
        self.data_vacancies = []
        self.html = None

    def get_html(self):
        response = requests.get(self.url)
        # html = response.text
        self.html = response.text
        # return html

    def pars_html(self):
        self.get_html()
        soup = Bs(self.html, 'parser.html')
        data = soup.find_all('table',class_='weather')
        self.data_weather = {'data': data}
        # return data

    def write_data_to_file(self):
        with open ('file.txt', 'w') as f:
            json.dump(self.data_weather, f, indent=2)

parser_weather = Parser(url='www.weather.com')
# html = parser_weather.get_html()
# data = parser_weather.pars_html(html)
parser_weather.pars_html()




