# Creación de la función
def Favorite_teacher_program():
    print("\tWelcome to the Favorite Teachers Program")
    fav_teachers = []

    for i in range(1,5):
        teacher = input(f"\tWho is your number {i} favorite teacher:\t")
        fav_teachers.append(teacher)

    print(f"\tYour favorite teachers ranked are: {fav_teachers}")
    print(f"\tYour favorite teacher alphabetically order are: {sorted(fav_teachers)}")
    print(f"\tYour favorite teacher alphabetically order are: {sorted(fav_teachers, reverse=True)}")
    print(f"\tYour top two teachers are: {fav_teachers[:2]}")
    print(f"\tYour next two teachers are: {fav_teachers[2:4]}")
    print(f"\tYour last favorite teacher is: {fav_teachers[len(fav_teachers)-1]}")
    print(f"\tYour have a total of 4 favorite teachers.")
    print(f"\tOops, {fav_teachers[0]} is no longer your favorite teacher.")

    new_teacher  = input("\tWho is your new FAVORITE teacher:\t")

    fav_teachers.insert(0,new_teacher)
    print(f"\tYour top two teachers are: {fav_teachers[:2]}")
    print(f"\tYour next two teachers are: {fav_teachers[2:4]}")
    print(f"\tYour last favorite teacher is: {fav_teachers[len(fav_teachers)-1]}")
    print(f"\tYour have a total of 5 favorite teachers.")


# Llamada a la función
Favorite_teacher_program()