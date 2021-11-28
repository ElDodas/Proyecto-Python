# Creación de la función
def frequency_analysis_app():
    import collections as collec
    print("\n\tWelcome the Frequency Analysis app\n")

    non_letters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ",
                ".", "?", "!", ",","\'","\"" , ":", ";", "(", ")", "%", "$", "&", "#", "\n", "\t"]

    for i in range(1,3):
        phrase = input("\n\tEnter a word or phrase to count the occurrence of each letter:\t").lower().strip()

        for character in non_letters:
            phrase = phrase.replace(character,"")

        letter_count = collec.Counter(phrase)
        total_occurences = len(phrase)

        print("\n\tHere is the frequency analysis from key phrase: ")
        print("\n\tLetter\t\tOccurrence\tPercentage")
        
        for char, count in sorted(letter_count.items()):
            print(
                    f"\t{char}\t\t {count} \t\t {round((count/total_occurences)*100,2)}%")

        ordered_letter_count = letter_count.most_common()
        user_phrase_1_ordered_letters = []
        for pair in ordered_letter_count:
            user_phrase_1_ordered_letters.append(pair[0])
        
        
        print("\n\tLetters ordered from highest occurrence to lowest: ")
        for letter in user_phrase_1_ordered_letters:
            print(letter, end="")
        print(f"\n")
        
# Llamada a la funcion
frequency_analysis_app()