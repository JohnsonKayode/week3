# Creating a class in python
# class student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

# person1 = student("Kayode", 30, 'E')

# print(person1.grade)

# # use the try and except block to handle errors
# person.course = 'History'
# print(person.course)

class Account:
    def __init__(self, account_holder, account_number, account_type, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f'{amount} withdrawn successfully.'
        else:
            print(f'You have insufficient balance, Your account balance is {self.balance}')

    def get_balance(self):
        return self.balance
    
    def get_account_type(self):
        return self.account_type
    
    def get_account_number(self):
        return self.account_number
    
    def get_account_details(self):
        return f' Account name:{self.account_holder},\n Account Number:{self.account_number},\n Account Type:{self.account_type},'
    
class CurrentAccount(Account):
    def get_account_details(self):
        return f'Account name:{self.account_holder},\n Account Number:{self.account_number},\n Account Type:{self.account_type},\n Current Account Balance: {self.balance}'
    
class SavingAccount(Account):
    def get_account_details(self):
        return f' Account name:{self.account_holder},\n Account Number:{self.account_number},\n Account Type:{self.account_type},\n Savings Account Balance (STUDENT): {self.balance}'
    


while True:
    # firstUser = ''
    firstUser_account_type = account_type = input('Enter 1. for Savings or 2 for Current. or type "done" to Exit: ')

    if account_type == '1':
        firstUser_account_type = account_type = 'Savings Account'  
        firstUser_account_holder = account_holder = input('Enter your name or type "done" to Exit: ')
        firstUser_account_number = account_number = input('Enter your account number or type "done" to Exit: ')
        firstUser_deposit_amount = deposit_amount = int(input('Enter your deposit amount or type "done" to Exit: '))
        firstUser = SavingAccount(firstUser_account_holder, firstUser_account_number, firstUser_account_type, firstUser_deposit_amount)
        print(firstUser.get_account_details())

        continuation = input('Do you want to perform any other task? (yes/done): ')
        if continuation == 'done':
            break
        else:
            while True:
                nextPrompt = input('Would you like to "withdraw" or "deposit" into your account? Or type "done" to exit: ')
                if nextPrompt == 'withdraw':
                    withdrawal = int(input('Enter the amount you want to withdraw: '))
                    withdrawal = firstUser.withdraw(withdrawal)
                    print(firstUser.get_account_details())
                elif nextPrompt == 'deposit':
                    deposit = int(input('Enter the amount you want to deposit: '))
                    firstUser.deposit(deposit)
                    print(firstUser.get_account_details())
                elif nextPrompt == 'done':
                    print('Exiting the program.')
                    break
                continuation = input('Do you want to perform any other task? (yes/done): ')
                if continuation == 'done':
                    print('Exiting the program.')
                    break
            break


    elif account_type == '2': 
        firstUser_account_type = account_type = 'Current Account'
        firstUser_account_holder = account_holder = input('Enter your name or type "done" to Exit: ')
        firstUser_account_number = account_number = input('Enter your account number or type "done" to Exit: ')
        firstUser_deposit_amount = deposit_amount = int(input('Enter your deposit amount or type "done" to Exit: '))
        firstUser = CurrentAccount(firstUser_account_holder, firstUser_account_number, firstUser_account_type, firstUser_deposit_amount)
        print(firstUser.get_account_details())

        continuation = input('Do you want to perform any other task? (yes/done): ')
        if continuation == 'done':
            break
        else:
            while True:
                nextPrompt = input('Would you like to withdraw or deposit into your account? Or type "done" to exit: ')
                if nextPrompt == 'withdraw':
                    withdrawal = int(input('Enter the amount you want to withdraw: '))
                    withdrawal = firstUser.withdraw(withdrawal)
                    print(firstUser.get_account_details())
                elif nextPrompt == 'deposit':
                    deposit = int(input('Enter the amount you want to deposit: '))
                    firstUser.deposit(deposit)
                    print(firstUser.get_account_details())
                elif nextPrompt == 'done':
                    print('Exiting the program.')
                    break
                continuation = input('Do you want to perform any other task? (yes/done): ')
                if continuation == 'done':
                    print('Exiting the program.')
                    break
            break

    elif account_type == 'done':
        print('Exiting the program.')
        break
    # else:
    #     print('Invalid account type. Please enter either "Savings" or "Current" or "done".')
    #     continue

    # firstUser = account_type(account_holder, account_number, account_type, deposit_amount)

    





# firstUser = SavingAccount('Johnson Kayode', '0235166515', 'Savings', 1000)
# firstUser.withdraw(500)
# print(firstUser.get_balance())


# firstUser.withdraw(50)
# print(firstUser.get_balance())
# print(firstUser.get_account_details())