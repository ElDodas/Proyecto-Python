# Creación de la función

def Grocery_list():
    import datetime
    time = datetime.datetime.now()
    print(f"""\tWelcome to the Grocery List App.
    \tCurrent Date and Time: {str(time.month)}/{str(time.day)} {str(time.hour)}:{str(time.minute)}
    \tYou cunrrently have Meat and Cheese in your list.""")

    food1 = input("\n\tType of food to add to the grocery list:\t").title()
    food2 = input("\tType of food to add to the grocery list:\t").title()
    food3 = input("\tType of food to add to the grocery list:\t").title()

    groce_list = ["Meat", "Cheese", food1, food2, food3]
    print(f"\n\tHere is your grocery list:\n\t{groce_list}\n\tHere is your grocery list sorted:\n\t{sorted(groce_list)}")
    print(f"\n\tSimulating grocery shopping...")

    print(f"\n\tCurrent grocery list: {len(groce_list)} items")
    print(f"\t{groce_list}")
    rm1 = input(f"\tWhat food did you just buy:\t").title()
    groce_list.remove(rm1)
    print(f"\tRemoving {rm1} from list...")

    print(f"\n\tCurrent grocery list: {len(groce_list)} items")
    print(f"\t{groce_list}")
    rm2 = input(f"\tWhat food did you just buy:\t").title()
    groce_list.remove(rm2)
    print(f"\tRemoving {rm2} from list...")

    print(f"\n\tCurrent grocery list: {len(groce_list)} items")
    print(f"\t{groce_list}")
    rm3 = input(f"\tWhat food did you just buy:\t").title()
    groce_list.remove(rm3)
    print(f"\tRemoving {rm3} from list...")

    print(f"\n\tCurrent grocery list: {len(groce_list)} items")
    print(f"\n\t{groce_list}")
    print(f"\n\tSorry, the store is out of Meat")
    groce_list.remove('Meat')
    add = input(f"\tWhat food would you like instead:\t").title()
    groce_list.append(add)

    print(f"\n\tHere is what remains on your grocery list:\t")
    print(f"\t{groce_list}")

# LLamada a la función
Grocery_list()