# coding: UTF-8
"""
Script: PenduGame/menu
Création: jojo, le 12/10/2024
"""
# Imports
import logging, utils
from cgi import print_environ_usage

import main as m
from Main.RpgLordOfRings.utils import show_tag

# Configurations globales
logging.getLogger().setLevel(logging.DEBUG)


# Fonctions
def show_menu_principal(menu: str = "P"):
    if menu == "P":
        show_tag()
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
        show_tag()
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