def vote_registration_app():
    print(f"\tWelcome to the Voter Registration App")

    name = input(f"\tPlease enter your name:\t")
    age = int(input(f"\tPlease enter your age:\t"))

    if age >= 18:
        print(f"\n\tCongratulations {name}! You are old enough to register to vote.\n")
        print(f"""\t\t-Republican
        \t-Democratic
        \t-Independent
        \t-Libertarian
        \t-Green\n""")
        party = input(f"\tWhat party would you like to join:\t").lower()

        if party == "republican" or party == "democratic":
            print(f"\tCongratulations {name}! You have joined the {party.title()} party!\n\tThat is a major party!")
        elif party == "independent":
            print(f"\tCongratulations {name}! You have joined the {party.title()} party!\n\tYou are an independent person!")
        else:
            print(f"\tCongratulations {name}! You have joined the {party.title()} party!\n\tThat is not a major party!")
    else:
        print(f"\tYou are not old enough to register vote")

vote_registration_app()