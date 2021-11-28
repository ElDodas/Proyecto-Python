# Creación de la función
def Summary_table():

    num_strings = ["15", "100", "55", "42"]
    num_ints = [15, 100, 55, 42]
    num_floats = [15.15, 100.10, 55.55, 42.42]
    num_lists = [[1,2,3],[4,5,6],[7,8,9]]

    print(f"\t\t\tSummary Table\n")

    print(f"\tThe variable num_strings is a {type(num_strings)}")
    print(f"\tIt contains the elements: {num_strings}")
    print(f"\tThe element {num_strings[0]} is a {type(num_strings[0])}\n")

    print(f"\tThe variable num_ints is a {type(num_ints)}")
    print(f"\tIt contains the elements: {num_ints}")
    print(f"\tThe element {num_ints[0]} is a {type(num_ints[0])}\n")

    print(f"\tThe variable num_floats is a {type(num_floats)}")
    print(f"\tIt contains the elements: {num_floats}")
    print(f"\tThe element {num_floats[0]} is a {type(num_floats[0])}\n")

    print(f"\tThe variable num_lists is a {type(num_lists)}")
    print(f"\tIt contains the elements: {num_lists}")
    print(f"\tThe element {num_lists[0]} is a {type(num_lists[0])}\n")

    print(f"\tNow sorting num_string and num_ints...")
    print(f"\tSorted num_string: {sorted(num_strings)}")
    print(f"\tSorted num_ints: {sorted(num_ints)}")

    print(f"\n\tStrings are sorted alphabetically while integers are sorted numerically!")

# Llamada a la función
Summary_table()