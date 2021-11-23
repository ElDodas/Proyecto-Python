# Creación de la función
def letter_counter_app():

    print("\tWelcome to the Letter counter App")

    name = input("\tWhat is your name:\t").capitalize()
    print(f"\tHello {name}")
    print("\tI will count the number of times that a specific letter occurs in a message.\n")

    message = input("\tPlease enter a message:\t")
    letter = input("\tWich letter would you like to count the occurrences of:\t")

    occurrences = message.count(letter)

    if occurrences > 1:
        s = "`s"
    else:
        s = ""

    print(f"\t{name}, your message has {occurrences} {letter}{s} in it ")

# Llamada a la función
letter_counter_app()