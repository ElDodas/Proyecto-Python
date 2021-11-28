# Creación de la función
def database_admin_program():
    print("\n Welcome to the Hasura Database ")

    log_on_information = {
        "admin00": "admin00",
        "user1": "user1user1",
        "user2": "user2user2",
        "user3": "user3user3",
        "user4": "user4user4",
        "user5": "user5user5"
    }

    username = input("\n\tEnter your user name :\t").lower()

    if username in log_on_information:
        password = input("\n\tEnter your password:\t")
        if password == log_on_information[username]:
            print(f"\n\tHello {username}! You`re now logged In")
            if username == "admin00":
                print(f"\n\tHere is the current user database:\t")
                for key, value in log_on_information.items():
                    print(f"\t{key} - {value}")
            else:
                opc = input("\n\tWould you like to change your password? (y/n):\t").lower()
                if opc == "y":
                    new_password = input("\n\tWhat would you like your new password to be (8 characters long):\t")
                    if len(new_password) >= 8:
                        log_on_information[username] = new_password
                        print(f"\n\t{username} your password is {new_password}.")
                    else:
                        print(f"\n\t{new_password} not the minimun eight characters")
                else:
                    print("\n\tOk! GoodBye. You`re logged out!")
        else:
            print(f"\tPassword incorrect!")
    else:
        print("\n\tUsername not in database, goodbye")

# Llamada a la función
database_admin_program()