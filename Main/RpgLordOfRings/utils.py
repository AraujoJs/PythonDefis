# coding: UTF-8
"""
Script: PenduGame/utils
Création: jojo, le 12/10/2024
"""
# Imports
import logging, sys
from time import sleep
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

# Configurations globales
logging.getLogger().setLevel(logging.DEBUG)

# Fonctions
def show_tag():
    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    cprint(figlet_format('jojo & Nico', font='starwars'))

def taper_text(text: str, load: bool = False):
    if load:
        print("chargement...", end="", flush=True)
        sleep(2)
        print("\r", end="", flush=True)
    for letter in text:
        print(letter, end="")
        if letter in [",", ".", "?", "!"]:
            sleep(0.5)
        else:
            sleep(0.05)
