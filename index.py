import sys
import time
import numpy

class Atm:
    def __init__(self):
        self.name = "Channel Bank"
        self.branch = "New york"
        self.myBalance = 0.0
        self.customer_info = {}
        self.mainMenu()
        
    def mainMenu(self):
        print("- WELCOME TO  " + self.name + " " + self.branch)
        print("""

        - What would you like to do
        1. Open an account
        2. Perform Transaction
        3. Exit
        """)
        
        self.user = input(">>  ")
        if self.user == "1":
            self.openAccount()
        elif self.user == "2":
            if self.customer_info == {}:
                print("SORRY YOU DO NOT HAVE AN ACCOUNT WITH US \n CREATE AN ACCOUNT AND TRY AGAIN")
                self.mainMenu()
            else:
                self.performTransaction()
        elif self.user == "3":
            self.exit()
        else:
            print("Wrong Input, please try again")
            self.mainMenu()
            
    def openAccount(self):
        self.oneUser = []
        print("- WELCOME TO  " + self.name + " " + self.branch)
        self.user3 = ["Last Name", "First Name", "Other Name", "Age", "Phone No.", "Address"]
        for self.details in self.user3:
            self.user4 = input( self.details + ": ")
            self.oneUser.append(self.user4)
        print("please wait a bit for your account number")
        time.sleep(3)
        self.accNumber = int(numpy.random.random()*10000000000)
        print(self.accNumber)
        self.oneUser.append(self.accNumber)
        print("this is your account number")
        self.oneUser.append(self.myBalance)
        time.sleep(2)
        self.customer_info[self.accNumber] = self.oneUser
        self.setPin()
        
        
    def setPin(self):
        self.user9 = input("Now set in your new pincode \n>>>  ")
        time.sleep(1)
        self.user0 = (input("Confirm pincode \n>>>  "))
        if (self.user0 == self.user9) and  (self.user9 != "" and self.user0 != "") and (len(self.user9) == 4):
            print("You have successfully create an account/pincode with " + self.name + ("\nYou can now proceed to perform any transaction"))
            self.oneUser.append(self.user0)
            self.mainMenu()
        else:
            print("""
            We cannot process this pincode...
            It's either (1) the pin does not match
                        (2) the pin is either more or less than 4 digit
                        (2) you've input an empty string
                        (3) you've input a non-integer value
            Check and try again
            """)
            self.setPin()
        time.sleep(2)
        
    def performTransaction(self):
        print(self.customer_info)
        self.accNo = input("Enter your account number >>>  ")
        self.pin = input("Enter your pin >>>  ")
        time.sleep(2)
        if self.accNo in self.customer_info or self.oneUser[8] == self.pin:
            self.customer_info[self.accNo] = self.oneUser
            print(" ")
            print( "WELCOME " + self.oneUser[1].upper() + """
                    - What Transaction would you like to perform;
                    1.Withdrawal               2.Deposit
                    3.Check Balance            4.Recharge
                    5.Reset pincode            0.Exit  
                     
                    """)
            self.input0 = input(">>  ")
            if self.input0 == "1":   
                self.withdrawal()
            elif self.input0 == "2":
                self.deposit()
            elif self.input0 == "3":
                self.checkBalance()
            elif self.input0 == "4":
                self.recharge()
            elif self.input0 == "5":
                self.newPin()
            elif self.input0 == "0":
                self.exit()
            else:
                print("Invalid input")
                self.performTransaction()
            
       
