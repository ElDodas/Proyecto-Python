# Creación de la función 

def Grade_Sorter_App():

    print('\tWelcome to the Grade Sorter App!\n' )
    first = int(input('\tWhat is your first grade?(0-100):\t'))
    second = int(input('\tWhat is your second grade?(0-100):\t'))
    third= int(input('\tWhat is your third grade?(0-100):\t'))
    fourth = int(input('\tWhat is your fourth grade?(0-100):\t'))
    grades= []
    grades.append(first)
    grades.append(second)
    grades.append(third)
    grades.append(fourth)
    print(f'\n\tYour grades are: {grades}\n')
    reversed_grades = sorted(grades,reverse=True)
    print(f'\tYour grades from highest to lowest are: {reversed_grades}\n' )
    print(f'\tThe lowest two grades now be dropped.')
    print(f'\tRemoved grade: {reversed_grades.pop(3)}')
    print(f'\tRemoved grade: {reversed_grades.pop(2)}\n')
    print(f'\tYour remaining grades are: {reversed_grades}')
    print(f'\tNice work! Your highest grade is a:{reversed_grades[0]}')

# Llamada a la función
Grade_Sorter_App()