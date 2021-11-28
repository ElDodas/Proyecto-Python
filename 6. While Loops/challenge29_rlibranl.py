# Creación de la función
def guess_my_word_app():
    import random

    print("\tWelcome to the Guess My world app\n")

    game_dict = {
        "sports":["basketball", "baseball", "ping pong", "football", "golf", "tennis"],
        "colors":["blue", "red", "yellow", "black", "white", "green"],
        "movies":["avengers", "harry potter", "manolita", "spiderman", "hunger games", "lost", "focus"],
        "fruits":["apple", "banana", "orange", "melon", "strawberry", "kiwi", "watermelon"]
    }

    game_keys = list(game_dict.keys())
    condition = True

    while condition:
        categoria = game_keys[random.randint(0,len(game_keys)-1)]
        game_word = game_dict[categoria][random.randint(0,len(game_dict[categoria])-1)]
        word_length = len(list(game_word))
        blank_word = []
        for i in range(0, word_length):
            blank_word.append("-")
        print(f"\tGuess a {word_length} letter word from the following category: {categoria}")
        guess=""
        guess_count = 0
        while guess != game_word:
            blank_word_list = " ".join(blank_word)
            print(f"\n\tWord to guess {blank_word_list}")
            guess = input("\tMake a guess :").lower()
            guess_count +=1
            
            if guess_count == word_length + 1:
                print(f"\n\tToo many guesses. Correct word is {game_word}. Thank you for playing with us.")
                break

            if guess ==  game_word:
                print(f"\tCorrect! You guessed the word in {guess_count} guesses")
                break
            else:
                print("\tThat is not correct. Let us reveal a letter to help you!")
                condition2=True
                
                while condition2:
                    letter_index = random.randint(0,word_length-1)
                    if blank_word[letter_index] == "-":
                        blank_word[letter_index] = game_word[letter_index]
                        condition2=False           

        stop = input("\n\tDo you want to play again ? (y/n) : ").lower().strip()
        if stop.startswith("n"):
                condition = False
                print("\n\tThank you for playing our game.")

# Llamda a la función
guess_my_word_app()