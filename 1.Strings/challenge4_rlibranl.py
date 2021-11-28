# Creación de la función
def triangle_solver_app():

    print("\tWelcome to the Triangle Solver App")

    ladoA = float(input("\tDime el lado A del triángulo rectángulo:\t"))
    ladoB = float(input("\tDime el lado B del triángulo rectángulo:\t"))

    print(f"\tPara un triángulo de lados {ladoA} y {ladoB}, su hipotenusa es {round((ladoA**2+ladoB**2)**(1/2),3)} y su área es {(ladoB*ladoA)/2}")

# Llamada a la función
triangle_solver_app()