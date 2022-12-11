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