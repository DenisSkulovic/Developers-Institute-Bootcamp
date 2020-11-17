# Exercise 1: Bank Account
# Part I:

# Create a BankAccount class that contains the following attributes and methods:
# Owner
# Balance
# __init__ : initialize the two attributes
# deposit : accept the deposit only if it is positive
# withdraw : accept the withdraws if they don’t exceed the available balance (ie. the attribute)
# Part II: : Expand the bank account class

# Create a class Owner.
# Each owner has a credit card number and a password. (ie. the attributes)
# Create a method check_owner_info that checks the credit card number and the password.
# The owner has 2 chances to get the right password.
# If he didn’t get it, inform him that the card has been eaten by the machine, and delete the credit card number
# Only if he gets the right credit card number and the right password, you can ask him if he wants to “deposit” or to “withdraw”.
# The deposit method only accept bills of $20, $50, $100$.
# Ask the user how many of each bill he wants to deposit. If it answers all the requirements, inform him of the sum he deposited.
# Continue asking him if he want to deposit more bills until he refuses.
# The withdraw method only give back bills from $20 to $50.
# Bonus:

# Create a class called Bank.
# The Bank class can have maximum 10 clients (so 10 bank accounts ie objects of the BankAccount class)
# Create a method to check how much money the bank has depending on the actions of its clients.
# Inform the Bank Manager of the amount, the number of bills and their values

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Deposit amount has to be a positive number.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdraw amount has to be a positive number.")
        if amount > self.balance:
            raise ValueError("Withdrawal amount cannot exceed the balance amount.")
        self.balance -= amount

class Owner:

    def __init__(self, credit_card, password):
        self.credit_card = credit_card
        self.password = password

    def check_owner_info(self):
        chances = 2
        while chances > 0:
            crdt_crd = input("Enter your Credit Card Number")
            psswd = input("Enter your Password")
            if self.credit_card != crdt_crd:
                print("Credit Card Number is incorrect.")
                chances -= 1
            if self.password != psswd:
                print("Password is incorrect.")
                chances -= 1
            if (self.credit_card == crdt_crd) and (self.password == psswd):
                print("The machine has eaten your card.")
                self.credit_card = ''
                break
        print("Information is correct.")
