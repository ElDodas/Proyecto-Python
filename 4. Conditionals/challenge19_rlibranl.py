def guess_my_number_app():
    import random
    print(f"\tWelcome to the Guess My Number App")

    name = input(f"\tHello! What is your name:\t")
    print(f"\tWell {name}, I am thinking of a number between 1 and 20.")

    num = random.randint(1,20)

    condicion = True
    guesses = 1
    while guesses <= 5 and condicion:
        guess_num = int(input(f"\n\tTake a guess:\t"))
        if guess_num == num:
            guesses += 1
            print(f"\n\tGood job, {name}! You guessed my number in {guesses-1} guesses!")
            condicion = False
        elif guess_num < num:
            print(f"\n\tYour guess is too low")
            guesses += 1
        elif guess_num > num:
            print(f"\n\tYour guess is too high")
            guesses += 1
    
    if condicion:
        print(f"\n\tGame Over. The number thinking of was {num}")

guess_my_number_app()