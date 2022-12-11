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
        else:
            print("Invalid Credentials Provided")
            self.performTransaction()
            
    def newPin(self):
        self.input1 = input("Input your old pincode \n>>>  ")
        time.sleep(1)
        self.input2 = input("Now set in your new pincode \n>>>  ")
        time.sleep(1)
        self.input3 = input("Confirm new pincode \n>>>  ")
        if self.input3 == self.input2:
            print("You have successfully create a new pincode")
        else:
            print("The pincode does not match")
            self.setPin()
        self.performTransaction()
        
    def withdrawal(self):
        print("WELCOME", self.oneUser[1].upper())
        print("""
                How much would you like to withdraw:
                    1. 1,000         3. 10,000
                    2. 5,000         4. Other Amount(please indicate...)
                    0. back      
                """)
        self.withdraw1 = input(">> ")
        if self.withdraw1 == "1":
            if self.myBalance >= 1000:
                print("Please wait while we proccess your request...")
                time.sleep(3)
                print("PLEASE TAKE YOUR CASH \n1000")
                float(self.myBalance - 1000)
                print("Please wait for your receipt...")
                time.sleep(1)
                print("Receipt: \nDear Customer; \n    Amount withdrawed: #1000 \n    Balance: " + str(float(self.myBalance - 1000)))
            elif self.myBalance < 1000:
                print("INSUFFICIENT BALANCE")
                time.sleep(2)
                self.withdrawal()
            else:
                print("NVALID INPUT")
            time.sleep(3)
            self.performTransaction()
        elif self.withdraw1 == "2":
            if self.oneUser[7] >= 5000:
                print("Please wait while we proccess your request...")
                time.sleep(3)
                print("PLEASE TAKE YOUR CASH \n5000")
                float(self.myBalance - 5000)
                print("Please wait for your receipt...")
                time.sleep(1)
                print("Receipt: \nDear Customer; \n    Amount withdrawed: #5000 \n    Balance: " + st(float(self.myBalance - 5000)))
                time.sleep(3)
                self.performTransaction()
            elif self.oneUser[7] < 5000:
                print("INSUFFICIENT BALANCE")
                time.sleep(2)
                self.withdrawal()
            else:
                print("NVALID INPUT")
        elif self.withdraw1 == "3":
            if self.oneUser[7] >= 10000:
                print("Please wait while we proccess your request...")
                time.sleep(3)
                print("PLEASE TAKE YOUR CASH \n10000")
                float(self.myBalance - 10000)
                print("Please wait for your receipt...")
                time.sleep(3)
                print("Receipt: \nDear Customer; \n    Amount withdrawed: #10000 \n    Balance: " + str(float(self.myBalance - 10000)))
                time.sleep(3)
                self.performTransaction()
            elif self.oneUser[7] < 10000:
                print("INSUFFICIENT BALANCE")
                time.sleep(2)
                self.withdrawal()
            else:
                print("NVALID INPUT")
        elif self.withdraw1 == "4":
            self.withdraw2 = float(input("indicate here > "))
            if self.oneUser[7] >= self.withdraw2: 
                print("Please wait while we proccess your request...")
                time.sleep(3)
                print("PLEASE TAKE YOUR CASH \n" + str(self.withdraw2) + "\n \nPlease note that this ATM will not retract any cash")
                self.withdrawCal = float(self.oneUser[7] - self.withdraw2)
                self.customer_info[self.oneUser[6]][7] = self.withdrawCal
                print("Please wait for your receipt...")
                time.sleep(1)
                print("Receipt: \nDear Customer; \n    Amount withdrawed: #" + str(self.withdraw2) +"\n    Balance: " + str(self.withdrawCal))
                time.sleep(3)
                self.performTransaction()
            elif self.oneUser[7] < self.withdraw2:
                print("INSUFFICIENT BALANCE")
                time.sleep(2)
                self.withdrawal()
            else:
                print("NVALID INPUT")
                time.sleep(1)
                self.withdrawal()
        else:
            self.performTransaction()
            
    def deposit(self):
        self.deposited =  float(input("DEPOSIT, \nHow much would you like to deposit \n>> "))
        self.depositCal = float(self.oneUser[7] + self.deposited)
        self.customer_info[self.oneUser[6]][7] = self.depositCal
        print("Dear Customer; \n    Amount deposited: # " + str(self.deposited)  + "\n    Total Balance: #" + str(self.depositCal))
        print(self.customer_info)
        time.sleep(2)
        self.performTransaction()
