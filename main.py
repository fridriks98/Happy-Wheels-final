from Controller.Main_controller import Main_controller
from Repository.Cars_repo import Cars_repo
from Controller.Rent_controller import Rent_controller
from Utilizations.Arts import Arts
import os

def main():
    os.system("cls||clear")
    print_art_page = Arts()
    print_art_page.get_happy_wheels()
    print_art_page.get_car()
    start_program = Main_controller()
    start_program.main_page()

main()

