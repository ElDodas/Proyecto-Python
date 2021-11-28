# Creación de la función
def shipping_accounts_program():
    names = ["rodri","juan","pablo","pedro","lilo"]

    print(f"\n\tWelcome to the Shipping Accounts Program\n")

    name = input(f"\tHello, what is your username:\t").lower()

    if name in names:
        print(f"\n\tHello {name.title()}. Welcome back to your account.")
        print(f"\tCurrent shipping prices are as follows:\n")

        print(f"""\t\tShipping orders 0 to 100:\t\t $5.10 each
        \tShipping orders 100 to 500:\t\t $5.00 each
        \tShipping orders 500 to 1000:\t\t $4.95 each
        \tShipping orders over 1000:\t\t $4.80 each""")

        ships = int(input(f"\n\tHow many items would you like to ship:\t"))
        
        if ships > 0 and ships < 100:
            price = 5.10
        elif ships >= 100 and ships < 500:
            price = 5.00
        elif ships >= 500 and ships < 1000:
            price = 4.95
        elif ships >= 1000:
            price = 4.80

        print(f"\n\tTo ship {ships} items it will cost you ${round(ships*price,2)} at ${price} per item")

        ask = input(f"\tWould you like to place this order (y/n):\t").lower()

        if ask == "y":
            print(f"\tOkay. Shipping your {ships} items")
        else:
            print(f"\tOkay, no order is being placed at this time")

    else:
        print(f"\tSorry, you do not have an account with us. Goodbye\n")

# Llamada a la función
shipping_accounts_program()