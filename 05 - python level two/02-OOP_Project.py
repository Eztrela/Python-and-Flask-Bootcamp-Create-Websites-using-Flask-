####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class BankException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
    


class Account():
    def __init__(self,owner,balance = 0) -> None:
        self.balance = balance
        self.owner = owner
    
    def __repr__(self) -> str:
        return f'O Saldo da conta de {self.owner} é de R$ {self.balance:.2f}'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        
        try:
            assert amount <= self.balance
            self.balance -= amount
        except AssertionError:
            #ou raise BankException('Saldo Insuficiente')
            print('Saldo Insuficiente')
# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
acct1.owner




# 4. Show the account balance attribute
acct1.balance




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)



# ## Good job!
print(acct1)