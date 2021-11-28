def factorial_calculator_app():
    import math
    print(f"\tWelcome to the Factorial Calculator App\n")

    fact = int(input(f"\tWhat number would you like to compute the factorial of?\t"))
    factorial = 1

    for i in range(1,fact+1):

        if i == 1:
            print(f"\t{fact}! = 1*", end = "")
        
        elif i == fact:
            print(f"{i}\n")
        
        else:
            print(f"{i}*", end = "")

        factorial = factorial * i


    print(f"\n\tHere is the result from the math library:\n\tThe factorial of {fact} is {math.factorial(fact)}!\n")
    print(f"\tHere is the result from my own algorithm:\n\tThe factorial of {fact} is {math.factorial(fact)}!\n")
    print(f"\tIt is shown twice that {fact}! = {factorial} (with excitment)\n")

factorial_calculator_app()