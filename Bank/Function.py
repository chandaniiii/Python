from Storage import all_account
from ErrorHandling import DepositAmountError,AccountNumberError
from Bank import Bank

def findAccountByAccountNumber(acc_number):
    for account in all_account:
        if account.account_number == acc_number:
            return account
    else:
        raise AccountNumberError('No account found with the given number.')

def CreateAccount():
    name = input('Enter your name :')
    job = input('Enter your job title :')
    initial_amount = int(input('How much initial amount would you deposit?'))
    
    if initial_amount > 100:
        b = Bank(name,job,initial_amount)
        all_account.append(b)
        print('Your account has been created successfully!')
        print(f'Account has been created with name {name} and A/C no. {b.account_number}.\nRs.{initial_amount}')
    else:
        raise DepositAmountError('Initial amount must be greater than 100')