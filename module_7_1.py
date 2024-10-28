from itertools import product
from xml.sax.handler import property_dom_node
from xmlrpc.client import APPLICATION_ERROR


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        data = self.get_products()
        for i in products:
            if i.name in data:
                print(f'{i.name} already exists in the shop')
            else:
                file = open(self.__file_name, 'a')
                prod_ = f'{str(i)}\n'
                file.write(prod_)
                

shop = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
shop.add(p1, p2)
p3 = Product('Apple', 10.3, 'Fruits')
p4 = Product('Still water', 0.5, 'Drinks')
shop.add(p3, p4)
print(shop.get_products())
print(p1.__str__())
