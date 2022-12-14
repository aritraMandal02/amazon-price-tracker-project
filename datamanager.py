import pandas as pd
from product import Product
import warnings


class Tracker():

    def __init__(self):
        self.csv_data = pd.read_csv('products.csv')

    def update_data(self, index, update_param):
        for key, value in update_param.items():
            self.csv_data.loc[index, key] = value

    def add_product(self, product, updatemode=0):
        url = product.prod_url
        self.url_list = self.csv_data['url']
        if not updatemode:
            warnings.warn(
                "Warning Message: Running 'add_product' without setting updatemode = 1. Existing data will not be updated."
            )
        for i in range(len(self.url_list)):
            if url == self.url_list[i]:
                if updatemode:
                    self.update_data(i, product.product_details())
                    self.csv_data.to_csv('products.csv', index=False)
                return
        self.update_data(len(self.url_list), product.product_details())
        self.csv_data.to_csv('products.csv', index=False)

    def delete_product(self, urls):
        for url in urls:
            i = self.csv_data[self.csv_data['url'] == url].index
            self.csv_data.drop(i, inplace=True)
        self.csv_data.to_csv('products.csv', index=False)
        return 'deleted specified data'

    def update_all(self):
        self.url_list = self.csv_data['url']
        i = 0
        for url in self.url_list:
            update_params = Product(url).product_details()
            self.update_data(i, update_params)
            i += 1
        self.csv_data.to_csv('products.csv', index=False)
        return 'All data up-to-date'

    def delete_all(self):
        self.csv_data = self.csv_data[0:0]
        self.csv_data.to_csv('products.csv', index=False)
        return 'All data deleted'
