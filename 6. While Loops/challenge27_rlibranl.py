# Creación de la función
def even_odd_number_sorter_app():
    print("\tWelcome to the Even Odd Number App\n")
    condicion = True

    while condicion :
        user_input = input("\tEnter in a string of numbers separated by a comma (.) :\t").replace(" ","").split(",")
        evens = []
        odds = []

        print(f"\n\t----Result Summary----")
        for i in user_input:
            if int(i) % 2 == 0:
                print(f"\t\t{i} is even!")
                evens.append(int(i))
            else:
                print(f"\t\t{i} is odd!")
                odds.append(int(i))
        
        odds = sorted(odds)
        evens = sorted(evens)
        
        
        print(f"\n\tThe following {len(evens)} numbers are evens:")
        for i in evens:
            print(f"\t\t{i}")
        
        print(f"\n\tThe following {len(odds)} numbers are odds:")
        for i in odds:
            print(f"\t\t{i}")
        
        stop = input("\n\tWould you like to run the program again (y/n):\t").lower().strip()

        if stop.startswith("n"):
            condicion = False
            print("\tThank you for using the program. Goodbye.")

# Llamda a la función
even_odd_number_sorter_app()