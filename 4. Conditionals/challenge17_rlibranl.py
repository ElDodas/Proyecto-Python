def coin_toss_app():
    import random
    print(f"\tWelcome to the Coin Toss App\n")
    print(f"\tI will flip a coin a set number of times")

    flips = int(input(f"\tHow many times would you like me to flip the coin:\t"))
    ask = input(f"\tWould you like to see the result of each flip (y / n):\t").lower()
    heads = 0
    tails = 0
    flip_count = 0

    print(f"\n\tFlipping!!!\n")
    
    for i in range(1,flips+1):
        flip_count += 1

        coin = random.randint(0,1)
        if coin == 0:
            heads += 1
        else:
            tails += 1

        if ask == "y":
            if coin == 0:
                print(f"\tHEADS")
            else:
                print(f"\tTAILS")
        if heads == tails:
            print(f"\tAt {flip_count}, the number of heads and tails were equal at {heads} each")
    print(f"\n\tResults Of Flipping A Coin {flips} Times:\n")
    print(f"\tSide\t\tCount\t\tPercentage")
    print(f"\tHeads\t\t{heads}/{flips}\t\t{round((heads/flips)*100,2)}%")       
    print(f"\tTails\t\t{tails}/{flips}\t\t{round((tails/flips)*100,2)}%")

coin_toss_app()