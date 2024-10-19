#coding: UTF-8
"""
Script:Main / RpgLordOfRings / main
création: jojo, le 12 / 10 / 2024
"""
#Imports
import logging, menu

from Main.JeuDuPendu.pendu_game import games
from Main.RpgLordOfRings.menu import get_menu_choice

#Configurations globales
logging.getLogger().setLevel(logging.DEBUG)

#Fonctions



#Programme principal

def start_game(game = None):
	if game == None:
		menu.show_menu_principal("P")
		get_menu_choice()

def new_game(name):
	#TODO: créer nouveau game
	pass

def get_list_game_choice()->list:
	#TODO: retourner la liste des games sauvegardés
	pass

def get_list_game()->list:
	return []


def main():
	start_game()
	pass



if __name__== '__main__':
	main()
