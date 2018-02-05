class TextInterface:

    from Inventory import Product
    
    inventory_program = Product(name='Inventory 2000',inventory=['wallet', 'watches', 'cufflinks', 'ties', 'bow ties'])
    
    print(f'\nWellcome to inventory management "{inventory_program.name}"')
    print(f'\nFirst update the inventory')
    print(f'\nThere is no wallet, watches, cufflinks, ties, bow ties')
    
    while True:
        command = input('What would like you to do ? add stuff(s), add price(p)' + \
                        ' estimate the value of product(e), show stuff(f), end program(x) ')
        print()
        
        if command == 's':
            stuff = input('What product do you want to add to the inventory ? ')
            quantity = int(input('How many product do you want to add to the inventory ? '))
            inventory_program.add_stuff(stuff=stuff, quantity= quantity)
        elif command == 'p':
            stuff = input('What product do you want price ? ')
            price = int(input('Please, enter the price of product: '))
            inventory_program.add_price(stuff=stuff, price=price)
        elif command == 'e':
            stuff = input('The value of what product do you want to estimate ? ')
            quantity = int(input('How many products do you want to price ? '))
            equal = inventory_program.value_stuff(stuff=stuff, quantity=quantity)
            print()
            print(f'The value equal: {equal}')
        elif command == 'f':
            print(inventory_program.generation_table())
        elif command == 'x':
            print(f'Thank you for using "{inventory_program.name}"')
            break
        elif command != 's' or command != 'p':
            print(f'It is a wrong reference {command}')
    