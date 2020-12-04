import random as r

def get_info(filename):
    words = []
    file = open(filename, 'r')
    for i in file.readlines():
        words.append(i.rstrip())
    print (words)
    nr = int(r.uniform(0, len(words)))
    print (words[nr])



if __name__ == "__main__":
    print("Categorii disponibile: \n 1. Nume \n 2. Sport \n")
    user_category = int(input("Alege o categorie: "))
    if (user_category == 1):
        filename = 'nume'
    elif (user_category == 2):
        filename = 'sport'

    get_info(filename)