# coding: UTF-8
"""
Script: PenduGame/menu
Création: jojo, le 12/10/2024
"""
# Imports
import logging, utils

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

def get_valid_choice(type) -> str:
    races = {1: "Humain", 2: "Elfe", 3: "Nain", 4: "Hobbit"}
    classes = {1: "Guerrier", 2: "Mage", 3: "Archer", 4: "Clerc", 5: "Bard"}
    temp = 0
    if type == "race":
        while temp not in races.keys():
            taper_text("Choisissez: ")
            temp = int(input())
        return races[temp]

    elif type == "class":
        while temp not in classes.keys():
            taper_text("Choisissez: ")
            temp = int(input())
        return classes[temp]

def calc_points(balance, n_points) -> int:
    if n_points == 10:
        return balance
    if n_points > 10:
        balance -= 1
    if n_points > 11:
        balance -= 1
    if n_points > 12:
        balance -= 2
    if n_points > 13:
        balance -= 2
    if n_points > 14:
        balance -= 3
    if n_points > 15:
        balance -= 3
    if n_points > 16:
        balance -= 4
    if 17 <= n_points <= 18:
        balance -= 4
    return balance
def get_left_points(balance):
    custs = [(11, 1), (13, 2), (15, 3), (17, 4)]
    points = 10
    for value, cust in custs:
        if balance >= cust * 2:
            points = value + 1
            balance -= cust * 2
        elif balance >= cust:
            points = value
            break
        else:
            break
    return points

def show_menu_info(att):
    if att == "FOR":
        print("""
    - Force (FOR)
    
    La Force représente la puissance physique de votre personnage. 
Elle détermine les dégâts infligés lors des attaques au corps à 
corps et influence la capacité à porter des objets lourds ou à 
effectuer des actions nécessitant de la force brute, comme briser 
des portes ou soulever des charges.
""")
    if att == "DEX":
        print("""
    - Dextérité (DEX)
    
    La Dextérité mesure l'agilité, la précision et la vitesse de 
votre personnage. Un personnage avec une haute Dextérité sera plus 
précis lors des attaques à distance (comme les flèches ou les sorts)
et aura une meilleure capacité à éviter les attaques ennemies. Cela 
affecte également les compétences de furtivité et de manipulation 
d'objets.)
""")

    if att == "INT":
        print("""
    - Intelligence (INT)
    
    L'Intelligence reflète la capacité de votre personnage à comprendre 
et utiliser des connaissances, notamment dans le domaine de la magie. Un 
personnage intelligent sera plus efficace dans l'utilisation des sorts, 
la résolution d'énigmes et l'apprentissage de nouvelles compétences.
""")
    if att == "CON":
        print("""
    - Constitution (CON)
    
    La Constitution mesure la santé et la résistance physique de votre 
personnage. Une haute Constitution augmente les points de vie (PV) de 
votre personnage, améliorant sa survie en combat. Elle influence également
la résistance aux maladies, poisons et effets néfastes.
""")

    if att == "CHA":
        print("""
    - Charisme (CHA)
    
    Le Charisme évalue l'aptitude de votre personnage à interagir avec les 
autres. Un personnage charismatique sera plus convaincant lors de négociations, 
aura de meilleures chances de persuader les PNJ (personnages non joueurs) 
et pourra inspirer ou diriger d'autres personnages.
""")
    str(input("Tapez un caractère pour retourner: "))

def get_perso_status(balance) -> dict:
    status = {"FOR": 10, "DEX": 10, "INT": 10, "CON": 10, "CHA": 10}
    print("""
- Avoir un attribut à 10 ne coûte aucun point.
- Attributs de 11 à 12 : Chaque point au-dessus de 10 coûte 1 point.
- Attributs de 13 à 14 : Chaque point au-dessus de 12 coûte 2 points.
- Attributs de 15 à 16 : Chaque point au-dessus de 14 coûte 3 points.
- Attributs de 17 à 18 : Chaque point au-dessus de 16 coûte 4 points.
(si à la fin il vous reste des points, il vous sera ajouté au dernier attribut)
---------- Attributs:
    - Force
    - Dextérité
    - Intélligence
    - Constitution
    - Charisme
    
    [i] pour plus d'information pour chaque attribut.
--------------------------------------------------------------------------------
""")


    taper_text(f"\nDistribuez {balance} points entre les attributs suivants :\n")

    # Vérifications des valeurs saisis (si c'est > 8 et inf au n de points max pos d'ajout avec la balance act
    print(f"                                 Balance: {balance} points\n")
    taper_text("Force [i]: ")
    is_valid = False
    while not is_valid:
        c_for = input()
        if c_for == "i":
            show_menu_info("FOR")
            taper_text("Force [i]: ")

        else:
            c_for = int(c_for)
            is_valid = 10 <= c_for <= get_left_points(balance)
            if not is_valid:
                print("Tapez une valeur valide pour force: ", end="")
            else:
                new_balance = calc_points(balance, c_for)
                balance = new_balance
                status["FOR"] = c_for

    print(f"                                 Balance: {balance} points\n")
    taper_text("Dextérité [i]: ")
    is_valid = False
    while not is_valid:
        c_dex = input()
        if c_dex == "i":
            show_menu_info("DEX")
            taper_text("Dextérité [i]: ")
        else:
            c_dex = int(c_dex)
            is_valid = 10 <= c_dex <= get_left_points(balance)
            if not is_valid:
                print("Tapez une valeur valide pour dextérité: ", end="")
            else:
                new_balance = calc_points(balance, c_dex)
                balance = new_balance
                status["DEX"] = c_dex

    print(f"                                 Balance: {balance} points\n")
    taper_text("Intélligence [i]: ")
    is_valid = False
    while not is_valid:
        c_int = input()
        if c_int == "i":
            show_menu_info("INT")
            taper_text("Intéligence [i]: ")
        else:
            c_int = int(c_int)
            is_valid = 10 <= c_int <= get_left_points(balance)
            if not is_valid:
                print("Tapez une valeur valide pour intélligence: ", end="")
            else:
                new_balance = calc_points(balance, c_int)
                balance = new_balance
                status["INT"] = c_int

    print(f"                                 Balance: {balance} points\n")
    taper_text("Constituition [i]: ")
    is_valid = False
    while not is_valid:
        c_con = input()
        if c_con == "i":
            show_menu_info("CON")
            taper_text("Constituition [i]: ")
        else:
            c_con = int(c_con)
            is_valid = 10 <= c_con <= get_left_points(balance)
            if not is_valid:
                print("Tapez une valeur valide pour constituition: ", end="")
            else:
                new_balance = calc_points(balance, c_con)
                balance = new_balance
                status["CON"] = c_con

    print(f"                                 Balance: {balance} points\n")
    taper_text("Charisme [i]: ")
    is_valid = False
    while not is_valid:
        c_cha = input()
        if c_cha == "i":
            show_menu_info("CHA")
            taper_text("Charisme [i]: ")
        else:
            c_cha = int(c_cha)
            is_valid = 10 <= c_cha <= get_left_points(balance)
            if not is_valid:
                print("Tapez une valeur valide pour charisme: ", end="")
            else:
                new_balance = calc_points(balance, c_cha)
                if new_balance != 0:
                    print("Il vous sera ajouté les points restants automatiquement!")
                    c_cha = get_left_points(balance)
                    print(f"Il vous a été mis {c_cha} points pour charisme.")
                    new_balance = calc_points(balance, c_cha)
                balance = new_balance
                status["CHA"] = c_cha

    taper_text("votre personnage est prêt!", load=True)
    return status

def get_menu_create_choice():
    points_balance = 20
    perso = {"name": "", "race": "", "class": "", "status": {}}
    utils.taper_text("Entrez le nom de votre personnage: ")
    perso["name"] = str(input())

    utils.taper_text("Choisissez votre race : ")
    print("""\n
    1. Humain
    2. Elfe
    3. Nain
    4. Hobbit
""")
    perso["race"] = get_valid_choice("race")

    utils.taper_text("Choisissez votre classe : ")
    print("""\n
    1. Guerrier
    2. Mage
    3. Archer
    4. Clerc
    5. Bard
    """)
    perso["class"] = get_valid_choice("class")

    perso["status"] = get_perso_status(points_balance)

    return perso


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
        utils.taper_text(f"Partie {game_name} créée avec succès!\n", True)
        print(get_menu_create_choice())

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