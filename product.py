from bs4 import BeautifulSoup
import datetime as dt
from headers import HEADERS
import requests


class Product(BeautifulSoup):

    def __init__(self, url, name=None):
        response = requests.get(url=url, headers=HEADERS)
        content = response.text
        super().__init__(content, 'lxml')
        self.prod_url = url
        if name is None:
            self.prod_name = self.get_prod_name()
        self.prod_rating = self.get_prod_rating()
        self.prod_price = self.get_prod_price()
        self.prod_date = dt.datetime.now().strftime('%d-%m-%Y')
        self.prod_time = dt.datetime.now().strftime('%I:%M:%S %p')

    def product_details(self):
        p_d = {
            'name': self.prod_name,
            'url': self.prod_url,
            'price': self.prod_price,
            'date': self.prod_date,
            'time': self.prod_time,
            'rating': self.prod_rating
        }
        return p_d

    def get_prod_price(self):
        return self.find(
            class_='a-price-whole').getText().split('.')[0].replace(',', '')

    def get_prod_name(self):
        return self.find(id='productTitle').getText().strip()

    def get_prod_rating(self):
        return self.find(class_='a-icon-alt').getText()
