#! python3

# main.py 
# A module where instances are defined

import wallet, vendingMachine

wallet_bal = wallet.Wallet()
v_machine = vendingMachine.VendingMachine()

invalid_selection = True
select_another_item = 'y'

while select_another_item == 'y':    
    print(f'current Bal: R{v_machine.wallet_bal.get_balance()}\n')
    v_machine.display_products()

    while invalid_selection:
        select_item = int(input('Pleases select item ->\n'))

        if select_item < 1 or select_item > v_machine.get_StockItems_size():
            print(f'Invalid selection! item: {select_item} is not listed. \n')
        else:
            invalid_selection = False

    print(f'Is available? {v_machine.check_availability(select_item)}')
    print(f'Can afford? {v_machine.check_funds(select_item)}')
    v_machine.dispense_product(select_item)
    select_another_item = input('Select another item? y-yes / n-no \n')
    invalid_selection = True

print('Thank you for using the user-riendly vending machinge. GOODBYE! :-)')



