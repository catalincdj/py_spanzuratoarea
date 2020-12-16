import random as r
from pathlib import Path
import json
import os

data_folder = Path("src/")
output_folder = Path("results/")

def get_categories(filename):
    categories = []
    file_to_open = data_folder / filename
    file = open(file_to_open, 'r')
    for i in file.readlines():
        categories.append(i.rstrip())
    file.close()
    return categories


def get_info(filename):
    words = []
    file_to_open = data_folder / filename
    file = open(file_to_open, 'r')
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

def solve_word(random_word, attempts, user_category, game_rounds, result_list):
    random_word = random_word.upper()
    new_word = init_word(random_word)
    user_attempts = 0
    wrong_attempts = 0
    
    for i in range(len(random_word)):
        if random_word[i] == new_word[0]:
            new_word[i] == random_word[i]
        elif random_word[i] == new_word[len(random_word) - 1]:
            new_word[i] = random_word[i]

    print("Indiciu: Cuvantul are {} litere: {}".format(len(new_word), ' '.join(new_word).upper()))
    initial_attempts = attempts
    correct_guess_attempts = 0
    while(attempts >= 0):
        user_guess_leter = input("Introduceti o litera: ").upper()
        for i in range(len(random_word)):
            if random_word[i] == user_guess_leter:
                new_word[i] = random_word[i]
                correct_guess_attempts += 1

        user_guess = ' '.join(new_word).upper()
        check_word = ''.join(new_word).upper()
        user_attempts += 1
        print(user_guess)
        if check_word == random_word:
            file_to_write = output_folder / "results.json"
            result_data = {"round": game_rounds, "category": user_category, "word": random_word, "attempts": user_attempts, "wrong-attempts": wrong_attempts}
            result_list.append(result_data)
            if os.stat(file_to_write).st_size == 0:
                with open(file_to_write, 'w') as json_file:
                    json.dump(result_list, json_file, indent = 4)
            else:
                with open(file_to_write, 'r') as json_read:
                    json_data = json.load(json_read)
                with open(file_to_write, 'w') as json_file:
                    json_data.append(result_list)
                    json.dump(result_list, json_file, indent = 4)
            return("\nFelicitari! Ai gasit cuvantul {} din {} incercari.".format(random_word, user_attempts))
        else:
            print("\nMai ai {} incercari ramase.".format(attempts))
            wrong_attempts = abs(user_attempts - correct_guess_attempts)
        attempts -= 1
        if attempts == 0:
            return("Imi pare rau, ai atins limita de {} incercari.".format(initial_attempts))
    user_guess = ''.join(new_word).upper()
    print(user_guess)


if __name__ == "__main__":
    game_rounds = 1
    result_list = []
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
        solution = solve_word(random_word, attempts, filename, game_rounds, result_list)
        print(solution)
        new_game = input("\nDoriti un nou cuvant? (da/nu): ")
        if new_game.lower() == 'da' or new_game.lower() == 'yes':
            print("Mult succes.")
            game_rounds += 1
            continue
        elif new_game.lower() == 'nu' or new_game.lower() == 'no':
            print("Joc incheiat.")
            exit(0)
    print(solution)