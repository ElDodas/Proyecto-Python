def rock_paper_scissors_app():
    import random
    moves = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    computer_action = random.choice(moves)

    plays = int(input(f"\tHow many rounds would you like to play:\t"))

    for i in range(1,plays+1):
        print(f"\tRound {i}")
        print(f"\tPlayer: {player_score}\tComputer: {computer_score}")
        player_action = input(f"\tTime to pick...rock, paper, scissors:\t").lower()
        
        if player_action != "rock" and player_action != "paper" and player_action != "scissors":
            print(f"\tThat is not a valid option")
        else:
            print(f"\tComputer: {computer_action}")
            print(f"\tPlayer: {computer_action}")

            if computer_action == player_action:
                print(f"\tIt is a tie, how boring!")
                winner = "tie"
            elif player_action == "rock":
                if computer_action == "scissors": # Player win
                    print(f"\tRock smash scissors!")
                    player_score += 1
                    winner = "player"
                else: # Computer win    
                    print(f"\tPaper cover rock!")
                    computer_score += 1
                    winner = "computer"

            elif player_action == "paper":
                if computer_action == "rock":  # Player win
                    print(f"\tPaper cover rock!")
                    player_score += 1
                    winner = "player"
                else: # Computer win    
                    print(f"\tScissors cut paper!")
                    computer_score += 1
                    winner = "computer"

            elif player_action == "scissors":
                if computer_action == "paper": # Player win
                    print(f"\tScissors cut paper!")
                    player_score += 1
                    winner = "player"
                else: # Computer win    
                    print(f"\tRock smash scissors!")
                    computer_score += 1
                    winner = "computer"

