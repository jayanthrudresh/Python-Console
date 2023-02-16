from sys import exit
from admin_login import admin
import user_login

class main:
    def __init__(self):
        self.__choice= 0

    def start(self):
        print("-----------------------------------Welcome--------------------------------------------")
        self.__choice=int(input("Please Enter Choice Given \n1.User login\n2.Admin login \n3.exit\nEnter Here: "))
        if self.__choice==1:
            user_login.choice_method()
        elif self.__choice==2:
            admin().admin_login()           
        else:
            exit
main().start()