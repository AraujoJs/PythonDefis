# coding: UTF-8
"""
Script: PenduGame/menu
Création: jojo, le 12/10/2024
"""
# Imports
import logging, utils
from os import PRIO_PGRP

import main as m
from Main.RpgLordOfRings.utils import taper_text

# Configurations globales§
logging.getLogger().setLevel(logging.DEBUG)


# Fonctions

# Création du personnage

def show_create_personnage():
    print("""
=====================================
\t\tCRÉATION DU PERSONNAGE
=====================================
""")

def get_menu_create_choice():
    races = {1: "Humain", 2: "Elfe", 3: "Nain", 4: "Hobbit"}
    classes = {1: "Guerrier", 2: "Mage", 3: "Archer", 4: "Clerc", 5: "Bard"}
    points_balance = 20

    utils.taper_text("Entrez le nom de votre personnage: ")
    name = str(input())
    utils.taper_text("Choisissez votre race : ")
    print("""\n
    1. Humain
    2. Elfe
    3. Nain
    4. Hobbit
""")
    utils.taper_text("Choisissez :")
    c_race = int(input())

    utils.taper_text("Choisissez votre classe : ")
    print("""\n
    1. Guerrier
    2. Mage
    3. Archer
    4. Clerc
    5. Bard
    """)
    taper_text("Choisissez :")
    choice = 0
    while choice not in [1, 2, 3, 4, 5]:
        choice = int(input())
    c_classe = classes[choice]

    print()
    taper_text("Distribuez 20 points entre les attributs suivants :")
    print()
    taper_text("Force (par défaut 5) :")
    c_force = int(input())
    print()
    taper_text("Agilité (par défault 5) :")
    c_agilitee = int(input())
    print()
    taper_text("Intelligence (par défault 5 :")
    taper_text("Défense (par défault 5 :")
    c_defense = int(input())

    taper_text("votre personnage est prêt!", load=True)

    return [c_classe, c_force, c_agilitee, c_defense]


def show_menu_principal(menu: str = "P"):
    if menu == "P":
        utils.show_tag()
        print("""
----- JDR Seigneur des anneaux -----
Un petit project créé par Jojo. Mon
premier text RPG. B1G2
=====================================
Bienvenue au menu principal.
A. Nouvelle partie
B. Charger partie
C. Options
D. Crédits
E. Quitter
=====================================
""")
    if menu == "A":
        print(
"""
=====================================
          NOUVELLE PARTIE
=====================================

""")
    if menu == "B":
        print(
"""
=====================================
        CHARGER UNE PARTIE
=====================================

Voice les parties sauvegardées disponibles:
"""
        )
        games = m.get_list_game()
        if len(games) == 0:
            print("         VIDE")
            go_to_main_menu()
        else:
            for i in range(len(games)):
                print(f"{i + 1}. {games[i]}")

    if menu == "C":
        print(
    """
=====================================
              OPTIONS
=====================================
        PAS ENCORE IMPLEMENTÉ!
    """)
        go_to_main_menu()
    if menu == "D":
        print(
    """
=====================================
              CRÉDITS
=====================================
Dévelopeur principal:
    - ARAUJO José 'jojocode'

Rémerciements Spéciaux:

Bibliothèques utilisées:

Inspiration:
    - Le fabulaux univers fantastique de J.R.R. Tolkien! Le seigneur des anneaux et le Hobbit. 
    - Ma passion pour les RPG et l'univers fantastique. 

Merci d'avoir joué a mon jeu! J'éspère que ça vous a plu! ;)
    """
        )
        utils.show_tag()
        go_to_main_menu()

def go_to_main_menu():
    print()
    input("Tapez un caractère pour retourner au menu principal: ")

def get_menu_choice() -> str:
    utils.taper_text("Choisissez une option: ")
    choice = " "
    choices = ["A", "B", "C", "D", "E"]
    while choice not in choices:
        choice = str(input()).upper()
        if choice not in choices:
            print("Tappez une option valide: ", end="")

    # Nouvelle partie
    if choice == "A":
        show_menu_principal("A")
        game_name = str(input("Entrez le nom de votre partie:"))
        m.new_game(game_name)
        utils.taper_text(f"Partie {game_name} créée avec succès!", True)

    elif choice == "B":
        show_menu_principal("B")
        game_choice = m.get_list_game()
        if len(game_choice) == 0:
            show_menu_principal()
            get_menu_choice()
        else:
            m.start_game(game_choice)
    elif choice == "C":
        show_menu_principal("C")
        show_menu_principal()
        get_menu_choice()
    elif choice == "D":
        show_menu_principal("D")
        show_menu_principal()
        get_menu_choice()
    elif choice == "E":
        print("Merci d'avoir joué!")
        print("=" * 16 + " FIM " + "="*16)