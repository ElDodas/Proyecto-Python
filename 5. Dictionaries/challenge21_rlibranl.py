# Creación de la función

def thesaurus_app():
    import random
    thesaurus = {"hot":["balmy","summery","tropical","boiling","scorching"],
                "cold":["chilly","cool","freezing","frigid","polar"],
                "happy":["content","cheery","merry","jovial","jocular"],
                "sad":["unhappy","downcast","miserable","glum","melancholy"]}
    
    print(f"\tWelcome to the Thesaurus App\n")
    print(f"\tChoose a word from the thesaurus and I will give you a synonym")
    
    print(f"\tHere are the words in the the thesaurus:")
    
    for key in thesaurus.keys():
        print(f"\t- {key}")
    word = input("\n\tPick a word you want synonym for :\t").lower()
    
    random_synom = random.randint(0,4)
    if word in thesaurus:
        print(f"\n\tA synonym  for {word} is {thesaurus[word][random_synom]}")
        response = input("\n\tWould you like to see complete thesaurus ? (y/n)\t").lower()
        if response == "y":
            for key, values in thesaurus.items():
                print(f"\n\tWord {key} is synonym to : ")
                for value in values:
                    print(f"\t- {value}")
        else:
            print("\tI hope you enjoyed the program. Thank you!")    
    else:
        print(f"\tI`m sorry, that word is not currently in the thesaurus")

# Llamada a la función
thesaurus_app()