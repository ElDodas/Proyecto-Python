#Creación de la función
def multiplication_exponent_table():
    name = input("\tWhats is your name?:\t").title()
    number = float(input("\tWhat number would you like to work with?:\t").title())

    print(f"""\n\tMultiplication table for {number}\n
        \t\t1.0*{number} = {round(1*number,4)}
        \t\t2.0*{number} = {round(2*number,4)}
        \t\t3.0*{number} = {round(3*number,4)}
        \t\t4.0*{number} = {round(4*number,4)}
        \t\t5.0*{number} = {round(5*number,4)}
        \t\t6.0*{number} = {round(6*number,4)}
        \t\t7.0*{number} = {round(7*number,4)}
        \t\t8.0*{number} = {round(8*number,4)}
        \t\t9.0*{number} = {round(9*number,4)}""")

    print(f"""\n\tExponent table for {number}\n
        \t\t{number}**1 = {round(number**1,4)}
        \t\t{number}**2 = {round(number**2,4)}
        \t\t{number}**3 = {round(number**3,4)}
        \t\t{number}**4 = {round(number**4,4)}
        \t\t{number}**5 = {round(number**5,4)}
        \t\t{number}**6 = {round(number**6,4)}
        \t\t{number}**7 = {round(number**7,4)}
        \t\t{number}**8 = {round(number**8,4)}
        \t\t{number}**9 = {round(number**9,4)}""")
    msg = "Math is cool!"
    print(f"""\n\t{name} {msg}
        \t\t{name.lower()} {msg.lower()}
        \t\t\t{name} {msg.title()}
        \t\t\t\t{name.upper()} {msg.upper()}""")

# Llamada a la función
multiplication_exponent_table()