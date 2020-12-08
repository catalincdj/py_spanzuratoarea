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
    nr = int(r.uniform(0, len(words)))
    random_word = words[nr]
    file.close()
    return random_word


def init_word(word):
    new_word = []
    for i in range(len(word) - 1):
        if i == 0:
            new_word.append(word[i])
        else:
            new_word.append('_')
    new_word.append(word[len(word) - 1])
    return new_word

def solve_word(random_word, attempts):
    random_word = random_word.upper()
    new_word = init_word(random_word)
    user_attempts = 0
    
    for i in range(len(random_word)):
        if random_word[i] == new_word[0]:
            new_word[i] == random_word[i]
        elif random_word[i] == new_word[len(random_word) - 1]:
            new_word[i] = random_word[i]

    print("Indiciu: Cuvantul are {} litere: {}".format(len(new_word), ' '.join(new_word).upper()))
    while(attempts > 0):
        user_guess_leter = input("Introduceti o litera: ").upper()
        for i in range(len(random_word)):
            if random_word[i] == user_guess_leter:
                new_word[i] = random_word[i]
        user_guess = ' '.join(new_word).upper()
        check_word = ''.join(new_word).upper()
        user_attempts = user_attempts + 1
        print(user_guess)
        if check_word == random_word:
            return("\nFelicitari! Ai gasit cuvantul {} din {} incercari.".format(random_word, user_attempts))
        else:
            print("\nMai ai {} incercari ramase.".format(attempts))
        attempts = attempts - 1
    user_guess = ''.join(new_word).upper()
    print(user_guess)


if __name__ == "__main__":
    while True:
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
        random_word = get_info(filename)

        ### Solve word with user input
        word_length = len(random_word)
        max_attepmts = word_length + word_length // 2
        word = list(random_word)
        new_word = init_word(word)

        attempts = max_attepmts
        solution = solve_word(random_word, attempts)
        print(solution)
        new_game = input("\nDoriti un nou cuvant? (da/nu): ")
        if new_game.lower() == 'da' or new_game.lower() == 'yes':
            print("Mult succes.")
            continue
        elif new_game.lower() == 'nu' or new_game.lower() == 'no':
            print("Joc incheiat.")
            exit(0)
    print(solution)