import random as r

def get_categories(filename):
    categories = []
    file = open(filename, 'r')
    for i in file.readlines():
        categories.append(i.rstrip())
    file.close()
    return categories


def get_info(filename):
    words = []
    file = open(filename, 'r')
    for i in file.readlines():
        words.append(i.rstrip())
    print (words)
    nr = int(r.uniform(0, len(words)))
    print (words[nr])
    file.close()


if __name__ == "__main__":
    ### Categories ###
    categories = get_categories("category")
    print("\nCategorii disponibile: ")
    for i in range(len(categories)):
        print('     {}. {}'.format(i + 1, categories[i]))

    ### User Input Category
    user_category = int(input("\nAlege o categorie: "))
    for i in range(len(categories)):
        if user_category == i + 1:
            filename = categories[i]

    ### Get words from choosen category
    get_info(filename)