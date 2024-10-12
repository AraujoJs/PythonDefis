from random import randint

nom_fichier = 'liste_francais.txt'
with open(nom_fichier, 'r', encoding='ISO-8859-1') as fichier:
    mots = [ligne.strip() for ligne in fichier.readlines()]


def genere_un_mot():
    a = randint(0, len(mots) - 1)
    caractere = True
    for v in mots[a]:
        if v in ['é', 'à', 'á', 'â', 'ç', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'û', '!', '?', "'"]:
            caractere = False

    if caractere:
        return mots[a]
    else:
        return genere_un_mot()

def dessiner_pendu(essais_restants):
    dessins = {
    8: """
           _____
           |   |
           |   Ø
           |  /|\\
           |  / \\
         __|_____
         |      |___
         |_________|
        """,
    7: """
           _____
           |   |
           |   O
           |  /|\\
           |  /
         __|____
         |      |___
         |_________|
        """,
    6: """
           _____
           |   |
           |   O
           |  /|\\
           |  
         __|_____
         |      |___
         |_________|
        """,
    5: """
           _____
           |   |
           |   O
           |  /|
           |  
         __|_____
         |      |___
         |_________|
        """,
    4: """
           _____
           |   |
           |   O
           |   |
           |  
         __|_____
         |      |___
         |_________|
        """,
    3: """
           _____
           |   |
           |   O
           |  
           |  
         __|_____
         |      |___
         |_________|
        """,
    2: """
           _____
           |   |
           |   
           |  
           |  
         __|_____
         |      |___
         |_________|
        """,
    1: """
           _____
           |   
           |   
           |  
           |  
         __|_____
         |      |___
         |_________|
        """,
    0: """

           |   
           |   
           |  
           |  
         __|_____
         |      |___
         |_________|   """,
    }

    print(dessins[essais_restants])


def tour(fautes,mot_devine,lettres_utilisees,mot):
    if fautes==8:
        dessiner_pendu(8)
        print(f"Vous avez perdu (noob), le mot était {mot} ")
        return False
    dessiner_pendu(fautes)
    print(" ")
    mot_devine_str=""
    for v in mot_devine:
        mot_devine_str=mot_devine_str+v
    print(f"Word:  {mot_devine_str} ({len(mot_devine_str)})")
    print(f"guessed letters/words:  {lettres_utilisees}")
    guess=input(f"Guess:  ")
    if guess==mot:
        return True
    for i in range(len(mot)):
        if guess not in lettres_utilisees:
            if mot[i]==guess:
                    for k in  range(len(mot_devine)):
                        if mot[k]==guess:
                            mot_devine[k]=guess
                    lettres_utilisees.append(guess)
                    mot_devine_str = ""
                    for v in mot_devine:
                        mot_devine_str = mot_devine_str + v
                    if mot_devine_str==mot: return print(f'Bravo le mot était {mot}, vous avez gagné avec {fautes} fautes !')
                    return tour(fautes, mot_devine, lettres_utilisees, mot)
        else:
            print('lettre/mot déjà essayée')
            return tour(fautes, mot_devine, lettres_utilisees, mot)
    print("Cette lettre/mot ne fait pas partie du mot")
    lettres_utilisees.append(guess)
    fautes += 1
    return tour(fautes, mot_devine, lettres_utilisees, mot)














def init():
    rep=input("Bienvenue dans ce pendu, voulez vous commencer ?")
    if rep=='oui':
        mot = genere_un_mot()
        fautes = 0
        lettres_utilisees=[]
        mot_devine=["-" for i in range(len(mot))]
        tour(fautes, mot_devine, lettres_utilisees, mot)




    else:
        print('Au revoir')
        return None

init()