from ErrorHandling import DepositAmountError,WithdrawAmountError



import random
class Bank:
    def __init__(self,name,job,initial_amount):
        self.name = name
        self.job = job
        self.initial_amount = initial_amount
        self.account_number = self.name[1:3]+''.join(str(random.randint(1,9))for i in range(16))+'NB'


    def deposit_amount(self,amount):
        if amount >= 100:
            self.initial_amount += amount
            print(f'{amount} has been deposited into A/C {self.account_number}')

        else:
            raise DepositAmountError('Deposit amount must be greater than  100')

    def withdrawAmount(self,amount):
        if amount <= self.initial_amount:
            self.initial_amount -= amount
            print(f'{amount} has been withdrawn from A/C {self.account_number}')
            print(self.initial_amount)
        else:
            raise WithdrawAmountError('Insufficient Balance ')

    def show_details(self):
            print(f'Name : {self.name}')
            print(f'Job : {self.job}')
            print(f'Initial Amount : {self.initial_amount}')
            print(f'Account No : {self.account_number}')

    