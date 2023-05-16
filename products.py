#! python3

# Products.py 
# data model for products

class Product:

    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def get_name(self) -> None:
        return self._name
    
    def get_price(self) -> None:
        return self._price

    def get_quantity(self):
        return self._quantity
    
    def set_quantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        rep = ''
        rep +=   f'name    : {self._name}\n'
        rep +=   f'price   : {self._price}\n'
        rep +=   f'quantity: {self.get_quantity()}\n'
        
        return rep
