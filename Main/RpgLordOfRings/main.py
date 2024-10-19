#coding: UTF-8
"""
Script:Main / RpgLordOfRings / main
création: jojo, le 12 / 10 / 2024
"""
#Imports
import logging, menu

#Configurations globales
logging.getLogger().setLevel(logging.DEBUG)

#Fonctions



#Programme principal

def start_game(game):
	games =[range(5)]

def new_game(name):
	#TODO: créer nouveau game
	pass

def get_list_game_choice()->list:
	#TODO: retourner la liste des games sauvegardés
	pass

def get_list_game()->list:
	return []


def main():
	menu.show_create_personnage()
	print(f"name: {menu.get_menu_create_choice()}")
	# menu.show_menu_principal()
	# menu.get_menu_choice()
	pass



if __name__== '__main__':
	main()
