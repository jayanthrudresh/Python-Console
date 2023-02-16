from time import sleep as wait
import datetime
from rich.console import Console
from rich.table import Table

class book:
    def __init__(self):
        self.__name=""
        self.__ser=0
        self.__date_time=""

    def booking(self):
        while(True):
            ser_name=["Scanning","X-ray","Testing"]
            self.__name=input("Enter Patient Name: ")
            self.__ser=int(input("Please enter \n0.Scanning\n1.X-ray\n2.Testing\nHere: "))
            self.__date_time=input("Enter date(date-month-year): ")
            try:
                datetime.datetime.strptime(self.__date_time, '%d-%m-%Y')
            except ValueError:
                print("Incorrect date string")
            else:
                if self.__ser>=0 and self.__ser<=len(ser_name):
                    table = Table(title="Booking Confirmed")
                    table.add_column("Name")
                    table.add_column("Service")
                    table.add_column("Date")
                    table.add_column("Token No")
                    console = Console()
                    file = open('booking.csv', 'r+')
                    for line in file:
                        item = line.split(',')
                        tok_no=item[3]
                    ntok_no=int(tok_no)+1
                    info = '\n' + self.__name + ',' + ser_name[self.__ser] + ',' + self.__date_time + ',' + str(ntok_no)
                    file.write(info)
                    file.close
                    table.add_row(self.__name,ser_name[self.__ser],self.__date_time,str(ntok_no),style='bright_green')
                    console.print("\n",table)
                    #print('{0} your {1} is scheduled on {2}'.format(name,ser_name[ser],date_time))
                    print("\n_____Thank You!_____")
                    wait(2)
                    break
                else:
                    print("wrong choice")