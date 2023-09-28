#! python3

# vendingMachine.py
# A module where transactions occur

import products, wallet

class VendingMachine:
    
    lstStockItems = [
        products.Product("Coke", 15.0, 5),
        products.Product("Chips", 8.0, 3),
        products.Product("Choco", 12.0, 5),
        products.Product("Lays", 8.0, 0),
        products.Product("Candy", 11.0, 5),
    ]
    productAvailable = True
    afford = True
    wallet_bal = wallet.Wallet()

    wallet_bal.set_balance(30.0)

    def get_StockItems_size(self) -> int:
        return len(self.lstStockItems)


    def display_products(self) -> None:
        for i in range(len(self.lstStockItems)):
            print(f'<-- it {i + 1} em -->')
            print(self.lstStockItems[i])

    def check_availability(self, choice) -> bool:
        self.productAvailable = False
        if self.lstStockItems[choice - 1].get_quantity() > 0:
            self.productAvailable = True
        return self.productAvailable
    
    def check_funds(self, choice) -> bool:
        self.afford = False
        if self.lstStockItems[choice - 1].get_price() <= self.wallet_bal.get_balance():
            self.afford = True
        return self.afford
    
    def dispense_product(self, choice) -> None:
        if not self.productAvailable:
            print('Item not avaialbe ..')
        if not self.afford:
            print('Insufficient funds!')         
        elif self.productAvailable == True and self.afford == True:
            new_bal = self.wallet_bal.get_balance() - self.lstStockItems[choice - 1].get_price() 
            self.wallet_bal.set_balance(new_bal)
            new_quantity = self.lstStockItems[choice - 1].get_quantity() - 1
            self.lstStockItems[choice - 1].set_quantity(new_quantity)
            print(f'{self.lstStockItems[choice - 1].get_name()} dispensing ...')
            print(f'new quantity: {self.lstStockItems[choice - 1].get_quantity()}')
            print(f'new balance: {self.wallet_bal.get_balance()}')
