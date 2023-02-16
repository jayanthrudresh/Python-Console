import maskpass
from view_details import view_details


class admin:
    def __init__(self):
        self.__email=""
        self.__password=""

    def admin_login(self):
        self.__email = str(input('Email: '))
        self.__password = str(maskpass.askpass(prompt='Password: ', mask="*"))    
        file = open('admin.csv', 'r')
        for line in file:
            item = line.split(',')
            if self.__email == item[0] and self.__password == item[1].strip():
                print('-----------------------------------Logged in successfully!---------------------------------\n')
                view_details.choice_view()   
        print("Sorry, you aren't signed up yet.")
        admin().admin_login()