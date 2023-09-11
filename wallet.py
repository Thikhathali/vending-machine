#! python3
# wallet.py 
# A data model where balance is kept

class Wallet:
    balance = 0.0

    def set_balance(self, bal):
        self.balance = bal

    def get_balance(self):
        return self.balance

    

