# Creación de la función
def fibonacci_calculator_app():
    print(f"\tWelcome to the Fibonacci Calculator App\n")
    fibo = int(input(f"\tHow many digits of the Fibonacci Sequence would you like to compute:\t"))
    print(f"\n\tThe first {fibo} numbers of the fibonacci sequence are:\n")

    fibo_nums = [1,1]
    golden_ratio = []

    # Printea la secuencia de números de fibonacci
    for i in range(1,fibo+1):
        if i == 1 or i == 2:
            print(f"\t{i} --> {fibo_nums[0]}")
        else:
            fibo_next = fibo_nums[len(fibo_nums)-1] + fibo_nums[len(fibo_nums)-2]
            fibo_nums.append(fibo_next)

            print(f"\t{i} --> {fibo_nums[len(fibo_nums)-1]}")

    print(f"\n\tThe corresponding Golden Ratio values are:\n")

    # Printea la secuencia de golden ratio
    for i in range(0,fibo-1):
        golden_next = fibo_nums[i+1] / fibo_nums[i]
        golden_ratio.append(golden_next)
        print(f"\t{i+1} --> {golden_ratio[len(golden_ratio)-1]}")
    
    print(f"\n\tThe ratio of consecutive Fibonacci terms approaches Phi; 1.618\n")  

# Llamada a la función
fibonacci_calculator_app()