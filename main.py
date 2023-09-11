#! python3

# main.py 
# A module where instances are defined

import wallet, vendingMachine

wallet_bal = wallet.Wallet()
v_machine = vendingMachine.VendingMachine()

select_another_item = 'y'

while select_another_item == 'y':    
    print(f'current Bal: R{v_machine.wallet_bal.get_balance()}\n')
    v_machine.display_products()

    select_item = int(input('Pleases select item ->\n'))
    print(f'Is available? {v_machine.check_availability(select_item)}')
    print(f'Can afford? {v_machine.check_funds(select_item)}')
    v_machine.dispense_product(select_item)
    select_another_item = input('Select another item? y-yes / n-no \n')

print('Thank you for using the user-riendly vending machinge. GOODBYE! :-)')



