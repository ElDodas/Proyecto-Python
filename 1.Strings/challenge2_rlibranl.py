# Creación de la función
def miles_per_hour_conversion_app():
    print("\tWelcome to the Miles Per Hour Conversion App")

    miles = float(input("\tWhat is your speed in miles per hour:\t"))

    kmXh = round(miles * 0.4474,2)

    print(f"\tYour speed in meters per second is: {kmXh}")

# Llamada a la función
miles_per_hour_conversion_app()