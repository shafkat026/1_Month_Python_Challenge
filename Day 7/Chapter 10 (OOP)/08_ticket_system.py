# import random
from random import randint

class train:

    def __init__(self, TrNo):
        self.TrNo = TrNo

    def book(self, fro, to):
        print(f"Ticket is booked in the Train No: {self.TrNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No: {self.TrNo} is on time.")

    def getFare(self, fro, to):   #as "from" is keyword
        print(f"Ticket Fare is: {randint(100,499)} in Train No: {self.TrNo} from {fro} to {to} is ")


t = train(702)
t.book("Dhaka", "Chattogram")
t.getStatus()
t.getFare("Dhaka", "Chattogram")