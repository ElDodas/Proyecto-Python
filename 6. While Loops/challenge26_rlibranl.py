# Creación de la función
def factor_generate_app():
    print("\tWelcome to the factor generator app.\n")
    condicion = True

    while condicion:
        user_input = int(input("\tEnter a number to determine all factors of that number:\t"))
        factors = []
        for i in range(1,user_input+1):
            if user_input % i == 0:
                factors.append(i)
        print(f"\n\tFactors of {user_input} are:\n")
        for i in factors:
            print(f"\t{i}")

        print(f"\n\tIn summary:")
        for i in range(int(len(factors)/2)):
            print(f"\t{factors[i]} * {factors[-i-1]} = {factors[i] * factors[-i-1]} ")

        stop = input("\n\tRun again ? (y/n):\t").lower()

        if stop.startswith("n"):
            condicion = False
            print("\tThank you for using the program. Have a great day.")

# Llamada a la función
factor_generate_app()