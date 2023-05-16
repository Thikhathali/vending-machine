#! python3
# wallet.py 
# A data model where balance is kept

class Wallet:
    _balance = 20.0

    def get_balance(self):
        return self._balance
    
    def set_balance(self, bal):
        self._balance = bal

    

