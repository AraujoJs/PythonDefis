# coding: UTF-8
"""
Script: Main/JeuDuPendu/pendu_game
Création: jojo, le 11/10/2024
"""
# Imports
import logging
from random import randint

# Configurations globales
logging.getLogger().setLevel(logging.DEBUG)

# Fonctions

words = [
    "chat", "soleil", "livre", "table", "fleur", "route", "pomme", "chien", "rêve", "porte",
    "jardinier", "ordinateur", "ballon", "chocolat", "magazine", "restaurant", "avion", "grenouille", "camembert",
    "bicyclette", "hippopotame", "télévision", "aspirateur", "incroyable", "bibliothèque", "parapluie", "champignon",
    "extraordinaire", "laboratoire"
]
global word, n_err, guessed, ref_word, c_average, o_average, is_ended
games = 1


def start_game():
    global word, n_err, guessed, ref_word, c_average, o_average, is_ended

    played = [-1]
    random_index = -1
    while random_index in played:
        if len(played) < len(words):
            random_index = randint(0, len(words) - 1)
        else:
            print("Plus de mots dispo ;(")
            break

    final_word = words[random_index]
    word = "_" * len(final_word)
    o_average = 0
    c_average = 0
    n_err = 0
    points = []
    guessed = " "
    ref_word = random_index
    is_ended = False

    while not is_ended:
        draw_pendu(n_err, guessed, word, ref_word, c_average, o_average, is_ended)
        guess = get_guess(guessed)
        guessed += guess
        if guess in final_word:
            indices = get_guess_indices(final_word, guess)
            c_average += get_current_average(points, len(indices))
            word = format_new_word(guess, indices)
        else:
            n_err += 1
            c_average += get_current_average(points, 0)

        if n_err == 6 or word == final_word:
            is_ended = True
            draw_pendu(n_err, guessed, word, ref_word, c_average, o_average, is_ended)
            o_average += c_average
            o_average /= games

            break
    print("-=-" * 25)


def get_current_average(points: list, times_letter) -> float:
    if times_letter == 0:
        points.append(-300)
    else:
        points.append(times_letter * 500)

    sum = 0
    for point in points:
        sum += point
    return sum / len(points)


def format_new_word(guess: str, indices: list) -> str:
    global word
    new_word = ""
    for i in range(len(word)):
        if i in indices:
            new_word += guess
        else:
            new_word += word[i]
    return new_word


def get_guess_indices(word: str, guess: str):
    indices = []
    for i in range(len(word)):
        if word[i] == guess:
            indices.append(i)

    return indices


def get_guess(guessed: str) -> str:
    guess = ""
    while guess in guessed or len(guess) != 1:
        guess = str(input("guess:"))
    return guess


def draw_pendu(n_err: int, guessed: str, word: str, ref_word: int, c_average: int, o_average: int, is_ended: bool):
    head = " "
    l_arm = " "
    r_arm = " "
    chest = " "
    l_leg = " "
    r_leg = " "
    final_message = ""
    ty = ""

    if is_ended:
        if n_err == 6:
            final_message = "VOUS AVEZ PERDU ;("
        else:
            final_message = "VOUS AVEZ GAGNÉ!!!!"
        ty = "by jojo. Merci d'avoir joué!"

    if n_err >= 1:
        head = "O"
    if n_err >= 2:
        chest = "|"
    if n_err >= 3:
        l_arm = "/"
    if n_err >= 4:
        r_arm = "\\"
    if n_err >= 5:
        l_leg = "/"
    if n_err == 6:
        r_leg = "\\"

    pendu = f"""
    
        ______
        |    |
        |    {head}                            Déviné: {guessed}
        |   {l_arm}{chest}{r_arm}                       
        |   {l_leg} {r_leg}                         Mot: #:            {ref_word}
        |                                   Moyenne Actuelle:    {c_average:.1f} points
      __|_____                              Moyenne Globale:    {o_average:.1f} points
      |       |___
      |__________|        {final_message}
                                {ty}
 mot: {word}
 """
    print(pendu)


# Programme principal
def main():
    global games
    is_ended = False

    while not is_ended:
        start_game()
        games += 1
        is_ended = input("Jouer de nouveau?[y/n]")[0].strip() == "n"
    # for i in range(7):
    #     draw_pendu(i, "aeiou", "a___e__", 1, 2000, 0, False)
    # pass


if __name__ == '__main__':
    main()
# Fin
