import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
from data.process import Process

class Data:
    def __init__(self):
        self.items = []  # Menyimpan item berupa dict {'name': str, 'price': float, 'quantity': int}

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def get_all_items(self):
        return self.items
