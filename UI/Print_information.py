from Models.Salesman import Salesman
from Repository.Salesman_repo import Salesman_repo
from Utilizations.Format_text import Format_text
import os

class Print_information(object):
    def __init__(self):
        self.main_header = "Press 'p' for Previous page\tPress 'm' for Menu\tPress 'x' to Exit"        

    def information_main_page(self, menu):
        """ Prints out the information window from main menu """
        os.system('cls||clear')
        print(self.main_header, end="\n\n")
        print(menu, end="\n\n")
        print("\t\t\t\tSmiðjuvellir 13")
        print("\t\t\t\tIS-300,Akranes")
        print("\t\t\t\tIceland\n")
        print("\t\t\t\tPhone: 431-6000")
        print("\t\t\t\thappywheels@happywheels.is\n")
        print("\t\t\t\tId.no: 651174-0289")
        print("\t\t\t\tTax nr: 14540\n")
        print("\t\t\t----- © 2018-2018 Happy Wheels. -----")
        print("\t\t\t\tA. Car Rental Agreement")
        print("\t\t\t\tB. Terms and Conditions")
        print("\t\t\t\tC. Quality Policy")
        print("\t\t\t\tD. List of Employees\n")
        choice = input("\t\t\t\tChoose an option: ").lower()
        return choice
    
    def car_rental_agreement(self):
        """ Prints out the Car Rental Agreement """
        os.system('cls||clear')
        print("By using our services you therefore agree to us\n using your information to better our services.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    def terms_and_conditions(self):
        """ Prints out Terms and Conditions """
        os.system('cls||clear')
        print("Terms and conditions")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("By using our services you therefore agree to us\n using your information to better our services.")
    
    def quality_policy(self):
        """ Prints out the Quality Policy """
        os.system('cls||clear')
        print("By using our services you therefore agree to us\n using your information to better our services.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    def print_salesman(self, name, email, ID):
        """ Prints out a list of Employees """
        print("Name: {:20} Email: {:30} ID: {:20}".format(name,email,ID))
        
    def print_salesman_header(self):
        """Prints header for salesman list"""
        os.system('cls||clear')
        print("\t\t\t~~Salesmen~~\n")

        
