def rock_paper_scissors_app():
    import random
    moves = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    computer_action = random.choice(moves)

    plays = int(input(f"\tHow many rounds would you like to play:\t"))

    for i in range(1,plays+1):
        print(f"\n\tRound {i}")
        print(f"\tPlayer: {player_score}\tComputer: {computer_score}")
        player_action = input(f"\tTime to pick...rock, paper, scissors:\t").lower()
        
        if player_action != "rock" and player_action != "paper" and player_action != "scissors":
            print(f"\tThat is not a valid option")
            print(f"\tComputer gets the point")
            computer_score += 1     
        else:
            print(f"\tComputer: {computer_action}")
            print(f"\tPlayer: {player_action}")

            if computer_action == player_action:
                print(f"\tIt is a tie, how boring!")
                print(f"\tThis round was a tie.")
            elif player_action == "rock":
                if computer_action == "scissors": # Player win
                    print(f"\tRock smash scissors!")
                    print(f"\tYou win round {i}")
                    player_score += 1
                else: # Computer win    
                    print(f"\tPaper cover rock!")
                    print(f"\tComputer wins round {i}")
                    computer_score += 1

            elif player_action == "paper":
                if computer_action == "rock":  # Player win
                    print(f"\tPaper cover rock!")
                    print(f"\tYou win round {i}")
                    player_score += 1
                else: # Computer win    
                    print(f"\tScissors cut paper!")
                    print(f"\tComputer wins round {i}")
                    computer_score += 1

            elif player_action == "scissors":
                if computer_action == "paper": # Player win
                    print(f"\tScissors cut paper!")
                    print(f"\tYou win round {i}")
                    player_score += 1
                else: # Computer win    
                    print(f"\tRock smash scissors!")
                    print(f"\tComputer wins round {i}")
                    computer_score += 1
    print(f"\n\n\tFinal Game Results")
    print(f"\t\tRounds Played: {plays}")
    print(f"\t\tPlayer Score: {player_score}")
    print(f"\t\tComputer Score: {computer_score}")
    
    if computer_score == player_score:
        print(f"\t\tIt was a tie\n")
    elif player_score > computer_score:
        print(f"\t\tWinner: PLAYER!!!\n")
    else:
        print(f"\t\tWinner: Computer :-(\n")

rock_paper_scissors_app()