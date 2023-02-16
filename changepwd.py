import re
import pandas as pd
import maskpass

class password:
    def __init__(self):
        self.__password = None

    def setpassword(self,email, password):
        try:
            self.__password = password
            df = pd.read_csv("accounts.csv", index_col="email")
            df.at[email, 'password'] =  self.__password
            df = df.reset_index()
            df.to_csv("accounts.csv", index=False)
            print("Note::\nYour Password Has Changed to :",self.__password)
        except:
            print("Somthing Went Wrong **Password not changed**")
def main():
    while True:
        pwd_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email=input("Enter Your Email: ")
        pwd_cmp = re.compile(pwd_reg) 
        if(re.fullmatch(email_regex, email)):
            file = open('accounts.csv', 'r+')
            for line in file:
                item = line.split(',')
                if (email==item[0]):
                    while True:
                        new_password=str(maskpass.askpass(prompt='Enter New Password: ', mask="*"))
                        if re.search(pwd_cmp,new_password):
                            password().setpassword(email,new_password)
                            exit(0)
                        else:
                            print("Please Enter Password correctly")
            else:
                print("Email Has Not Registered")
                break
        else:
            print("Please Check Your Email")
    file.close()