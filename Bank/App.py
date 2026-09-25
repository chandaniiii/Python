from ErrorHandling import DepositAmountError,WithdrawAmountError,AccountNumberError
from Function import CreateAccount,findAccountByAccountNumber
def bankApp():
    while True:
        print('1.Create Account')
        print('2.Deposit Account')
        print('3.Withdraw Account')
        print('4.User Details ')
        print('5.Exit ')

        choice = int(input('Enter Your Choice:'))

        if choice ==1:
            y_n = input('Do you want to create account? (Y/N)')

            if y_n == 'Y':
                print(f'{'*' * 45}')
                print('Create Account')
                print(f'{'*' * 45}')
                try:
                    CreateAccount()   
                except DepositAmountError as de:
                    print(f'{de}')
            else:
                print('Please continue with your transaction!')
                
        elif choice == 2:
            y_n = input('Do you want to deposit amount? (Y/N)')
            if y_n == 'Y':
                print(f'{'*' * 45}')
                print('Deposit Amount')
                print(f'{'*' * 45}')
                try:
                    acc_number = input('Enter your A/C no. :')
                    find_acc = findAccountByAccountNumber(acc_number)

                    if find_acc:
                        amount = int(input('Enter amount you want to deposit:'))
                        find_acc.deposit_amount(amount)
                        
                except DepositAmountError as de:
                    print(f'{de}')
                except AccountNumberError as ae:
                    print(f'{ae}')
            else:
                print('Please continue with your transaction!')
                
        
        elif choice == 3:
            y_n = input('Do you want to withdraw amount? (Y/N)')
            if y_n == 'Y':
                print(f'{'*' * 45}')
                print('Withdraw Amount')
                print(f'{'*' * 45}')
            
                try:
                    acc_number = input('Enter your A/C no. :')
                    find_acc = findAccountByAccountNumber(acc_number)

                    if find_acc:
                        print(f'Total amount = {find_acc.initial_amount}')
                        amount = int(input('Enter amount you want to withdraw:'))
                        find_acc.withdrawAmount(amount)
                        print(f'Remaining amount = {find_acc.initial_amount}')
                        
                except WithdrawAmountError as we:
                    print(f'{we}')
                except AccountNumberError as ae:
                    print(f'{ae}')
            else:
                print('Please continue with your transaction!')
                    
        
        elif choice == 4:
            y_n = input('Do you want to view your details? (Y/N)')
            if y_n == 'Y':
                print('*' * 45)
                print('User Details')
                print('*' * 45)
            
                try:
                    acc_number = input('Enter your A/C no. :')
                    find_acc = findAccountByAccountNumber(acc_number)

                    if find_acc:
                        find_acc.show_details()
                        
                    
                except AccountNumberError as ae:
                    print(f'{ae}')
            else:
                print('Please continue with your transaction!')
                    
        
        elif choice == 5:
            print('Thank you for your time')
            break

        else:
            print('Invalid Choice ')
        