
def quadratic_equation_solver_app():
    import cmath
    import math

    print("\tWelcome to the Quadratic Equation Solver App\n")
    print("\tA quadratic equation is of the form ax² + bx + c = 0")
    print("\tYour solution can be real or complex numbers.")
    print("\tA complex number hos two parts: a + bj")
    print("\tWhere a is the real portion and bj is the imaginary portion\n")

    num_equa = input(f"\tHow many equations would you like to solve today:\t")

    for i in range(1,int(num_equa)+1):
        
        print(f"\n\tSolving equation #{i}\n\t--------------------------\n")
        a = float(input(f"\tPlease enter your value of a (coefficent of x²):\t"))
        b = float(input(f"\tPlease enter your value of b (coefficent of x):\t"))
        c = float(input(f"\tPlease enter your value of c (coefficent):\t"))

        print(f"\n\tThe solutions to {a}x² + {b}x + {c} = 0 are:\n")
        
        # Hacemos la cuenta de dentro de la raíz
        sqrt = b**2 - 4*a*c

        if sqrt > 0: # Evalua que la raíz es mayor de 0

            x1 = (-b + math.sqrt(sqrt))/(2*a)
            x2 = (-b - math.sqrt(sqrt))/(2*a)

        elif sqrt == 0: # Evalua si la raíz es igual a 0

            x1 = (-b) / (2*a)
            x2 = None
        else: # Evalua que la raíz es mayor de 0
            
            x1 = (-b + cmath.sqrt(sqrt))/(2*a)
            x2 = (-b - cmath.sqrt(sqrt))/(2*a)

        # Muestra el resultado de la ecuación 
        print(f"\t x1 = {x1}\n\t x2 = {x2}")

    print(f"\n\tThanks you for using the Quadratic Equation Solver App. Goodbye")

quadratic_equation_solver_app()