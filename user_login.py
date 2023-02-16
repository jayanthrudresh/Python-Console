from sys import exit
import re
import maskpass
import booking
import changepwd

def choice_method():
    print("-----------------------------------Welcome User--------------------------------------------")
    while(True):
        print("Please Enter Choice Given \n1.Login\n2.Register\n3.Change Password\n4.Exit")
        try:
            choice=int(input("Enter Here: "))
        except:
            print("XXXXXX---Warning---XXXXXX\nPlease Follow The Instruction Correctly")
        else:
            if choice==1:
                auth.login()
                break
            elif choice==2:
                auth.sign_up()
                break
            elif choice==3:
                changepwd.main()
                break
            elif choice==4:
                exit
                break
            else:
                print("XXXXXX---Warning---XXXXXX\ninvalid choise\nEnter The Choice Correctly")

class auth:
    def login():
        email = str(input('Email: '))
        password = str(maskpass.askpass(prompt='Password: ', mask="*"))   
        file = open('accounts.csv', 'r')
        for line in file:
            item = line.split(',')
            if email == item[0] and password == item[1].strip():
                print('-----------------------------------Logged in successfully!---------------------------------\n')
                print('                              *********Booking Details*********                            ')
                booking.book().booking()
                exit(0)
        print("Sorry, you aren't signed up yet.")
        choice_method()

    def sign_up():
        while True:
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            pwd_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            ph_pattern = re.compile("(0|91)?[6-9][0-9]{9}")
            pwd_cmp = re.compile(pwd_reg)                
            email = str(input('Email: '))
            password = str(maskpass.askpass(prompt='Password: ', mask="*"))
            re_password= str(maskpass.askpass(prompt='Re-Enter Password: ', mask="*"))
            phone_no=input('Ph_No: ')
            if(re.fullmatch(email_regex, email) and re.search(pwd_cmp,password) and ph_pattern.match(phone_no)):
                if(password==re_password):
                    file = open('accounts.csv', 'a')
                    info = '\n' + email + ',' + password + ',' + phone_no
                    file.write(info)
                    print('Do you want to log in? [Yes/No]')
                    start_over = str(input()).lower()
                    file.close()
                    if 'y' in start_over:
                        auth.login()
                    else:
                        choice_method()
                        break
                else:
                   print("Password doesnot match")
            else:
                print("Please enter the valid email and password and ph number")