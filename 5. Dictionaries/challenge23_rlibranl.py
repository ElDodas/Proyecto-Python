# Creación de la función
def yes_or_no_polling_app():
    print("\n\tWelcome to the Yes or No Issue Polling App\n")
    poll_question = input("\tWhat is the yes or no issue you will be voting on today:\t").title()
    max_voters = int(input("\tWhat is the number of voters you will allow on the issue:\t"))
    master_password = input("\tEnter a password for polling results:\t").strip()

    yes_count = 0
    no_count = 0
    vote_result = {}

    for i in range(max_voters):
        voter_name = input("\n\tEnter your full name:\t").lower()
        if voter_name in vote_result:
            print("\tSorry, it seems that someone with that name has already voted.")
        else:
            print(f"\tHere is our issue: {poll_question}")
            voter_response = input("\tWhat do you think? (y/n):\t").lower( ).strip()
            if voter_response.startswith("y"):
                yes_count += 1
                vote_result.update({voter_name:"yes"})
            elif voter_response.startswith("n"):
                no_count += 1
                vote_result.update({voter_name:"no"})
            
            print(f"\tThank you {voter_name}! Your vote of {voter_response} has been recorded")

    print(f"\n\tThe following {max_voters} people voted valid:\n")
    for name in vote_result:
        print(f"\t{name}")
        
    print(f"\n\tOn the following issue: {poll_question}")
    if yes_count > no_count:
        print(f"\tYes wins! {yes_count} votes to {no_count}")
    elif yes_count < no_count:
        print(f"\tNo wins! {no_count} votes to {yes_count}")
    else: 
        print(f"\tIt was a tie {no_count} votes to {yes_count} ") 

    entered_password = input("\n\tTo see the voting results enter the admin password:\t").strip()
    if entered_password == master_password:
        for name, vote in vote_result.items():
            print(f"\tVoter:{name} - Vote:{vote}")
    else:
        print("\tSorry, that is not the correct password. Goodbye...")
        
    print("\n\tThank you for using the Yes or No Issue Polling App.")

# Llamada a la función
yes_or_no_polling_app()