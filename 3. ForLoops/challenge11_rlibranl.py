# Creación de la función
def binary_hexadecimal_converter_app():
    print("\tWelcome to the Binary/Hexadecimal")
    nums = input("\tCompute binary and hexadecimal values up to the following decimal number:\t")
    print("\tGenerating lists....complete!\n")
    print("\tUsing slices, we will now show a portion of each list.")
    start_num = int(input("\tWhat decimal number would you like to start at:\t"))
    stop_num = int(input("\tWhat decimal number would you like to stop at:\t"))

    lista_nums = range(1,int(nums)+1)
    
    # Creación listas binario y hexadecimal
    bin_list = []
    hex_list = []

    # Agregar a listas de binario y decimal
    for num in lista_nums:
        bin_list.append(bin(num))
        hex_list.append(hex(num))

    # Print decimal values
    print(f"\n\tDecimal values from {start_num} to {stop_num}")
    for dec_num in range(start_num-1,stop_num):
        print(f"\t{lista_nums[dec_num]}")

    # Print binary values
    print(f"\n\tBinary values from {start_num} to {stop_num}")
    for bin_num in range(start_num-1,stop_num):
        print(f"\t{bin_list[bin_num]}")

    # Print hexadecimal values
    print(f"\n\tHexadecimal values from {start_num} to {stop_num}")
    for hex_num in range(start_num-1,stop_num):
        print(f"\t{hex_list[hex_num]}")

    # Espera a que el usuario pulse una tecla
    stop = input(f"\n\tPress Enter to see values from 1 to {nums}")

    # Print de todos los valores de las listas anteriores
    print("\n\tDecimal---Binary---Hexadecimal\n\t------------------------------")
    for nums in range(0,int(nums)):
        print(f"\t{lista_nums[nums]} ---- {bin_list[nums]} ---- {hex_list[nums]}")

# Llamada a la función
binary_hexadecimal_converter_app()