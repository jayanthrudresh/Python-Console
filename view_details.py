from sys import exit
from rich.console import Console
from rich.table import Table


class view_details:
    @classmethod
    def __init__(self):
       self.__book_file=None
       self.__login_file=None

    def choice_view():
        while True:
            view=int(input("Please Enter to View \n1.Login Details\n2.Booking Details\n3.Exit\nHere: "))
            if view==1:
                view_details().login_details()
            elif view==2:
                view_details().booking_details()
            elif view==3:
                exit(0)
            else:
                print("Invalid Choice")     


    def booking_details(self):
        self.__book_file = open('booking.csv', 'r')
        table = Table(title="Booking Details")
        table.add_column("Name")
        table.add_column("Service")
        table.add_column("Date")
        table.add_column("Token")
        for line in self.__book_file:
            item = line.split(',')
            if item[2]!='date':
                table.add_row(item[0],item[1],item[2],item[3],style='bright_green')
        console = Console()
        console.print("\n",table)

    def login_details(self):
        self.__login_file = open('accounts.csv', 'r')
        table = Table(title="Login Details")
        table.add_column("Email")
        table.add_column("Phone no")
        for line in self.__login_file:
            item = line.split(',')
            if item[0]!='email':
                table.add_row(item[0],item[2],style='bright_green')
        console = Console()
        console.print("\n",table)