def grade_point_average_calculator_app():
    import statistics as stats
    print(f"\tWelcome to the Average Calculator App\n")

    name = input(f"\tWhat is your name:\t").title()
    num_of_grades = int(input(f"\tHow many grades would you like to enter:\t"))

    grades = []

    for i in range(1,num_of_grades+1):
        grade = int(input(f"\tEnter grade:\t"))
        grades.append(grade)

    print(f"\n\tGrades Highest to Lowest:")

    sort_grades = sorted(grades)
    for i in range(1,num_of_grades+1):
        print(f"\t\t{sort_grades[len(sort_grades)-i]}")

    print(f"\t{name}'s Grade Summary:")
    print(f"\t\tTotal Number of Grades: {num_of_grades}")
    print(f"\t\tHighest Grade: {max(sort_grades)}")
    print(f"\t\tLowest Grade: {min(sort_grades)}")
    print(f"\t\tAverage: {round(stats.mean(sort_grades),2)}")

    next_grade = int(input(f"\tWhat is your desired average:\t"))

    print(f"\tGood luck {name}")


grade_point_average_calculator_app()