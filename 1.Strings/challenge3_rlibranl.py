# Creación de la función
def temperature_conversion_app():

    print("\tWelcome to the Temperature Conversion App")

    fahrenheit = float(input(f"\tWhat is the given temperature in degrees Farenheit:\t"))

    print(f"\tDegrees Fahrenheit:\t{round(fahrenheit,2)}")
    print(f"\tDegrees Celsius:\t{round((fahrenheit - 32) * 5/9, 4)}")
    print(f"\tDegrees Kelvin:\t\t{round(((fahrenheit - 32) * 5/9) + 273.15, 4)}")

# Llamada a la función
temperature_conversion_app()