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
      