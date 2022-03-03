class User:
    def __init__(self, first_name, last_name, gender, street_address,
                 city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        users_list.append(self)

    def display_info(self):
        print('Full name:', self.first_name, self.last_name)
        print('Gender:', self.gender)
        print('Address:', self.street_address)
        print('Email:', self.email)
        print('CC number:', self.cc_number)
        print('CC type:', self.cc_type)
        print('Balance:', self.balance)
        print('Account no.:', self.account_no)
        print('*************************************************\n')

def generate_user():
    import csv
    with open ('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
        for line in filereader:
            line[8] = line[8].replace('$','') #remove the dollar sign
            line[8] = line[8].translate({ord(i): None for i in ','}) #remove the comma
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                 float(line[8]), line[9])

def find_user():
    is_user = False
    user_name = input('Name: ').title()

    for user in users_list:
        if user_name in user.first_name:
            user.display_info()
            is_user = True
        elif user_name in user.last_name:
            user.display_info()
            is_user = True

    if not is_user:
        print(f'There are no customers named "{user_name}" in the system.')

def overdrafts():
    total_amount = 0

    for user in users_list:
        if user.balance < 0:
            user.display_info()
            total_amount -= user.balance

    print('Total overdrafts amount: ${:.2f}'.format(total_amount))

def missing_email():
    count = 0

    for user in users_list:
        if not user.email:
            count += 1
            user.display_info()

    print(f'There are {count} people do not have a email address recorded')

def bank_details():
    count = 0
    amount = 0
    highest_balance = 0
    lowest_balance = 0
    highest_balance_user = ''
    lowest_balance_user = ''

    for user in users_list:
        count += 1
        amount += user.balance

        if user.balance >= highest_balance:
            highest_balance = user.balance
            highest_balance_user = user
        elif user.balance <= lowest_balance:
            lowest_balance = user.balance
            lowest_balance_user = user

    print(f'Total users: {count}\n'
          f'Bank total worth: {amount}')
    print()
    print('Highest balance account:')
    highest_balance_user.display_info()

    print('Lowest balance account:')
    lowest_balance_user.display_info()

def confirmation(account):
    for user in users_list:
        if account == user.cc_number:
            user.display_info()
            confirm = input('Confirm account? (Y/N): ').upper()

            if confirm == 'Y':
                return True, user
            else:
                return False

def transfer():
    valid = True
    account_error = 'This account does not exist in the system'
    main_info = ''
    sub_info = ''

    while valid:
        account = input('Enter your account number: ')
        main_info = confirmation(account)

        if main_info[0]:
            amount = float(input('Enter amount of money to transfer: $'))

            if amount <= main_info[1].balance:
                transfer_acc = input("Enter account's number to be transferred: ")
                sub_info = confirmation(transfer_acc)

                if sub_info[0]:
                    main_info[1].balance -= amount
                    sub_info[1].balance += amount

                    print('Transfer completed')

                    valid = False

                else:
                    print(account_error)
                    continue

            else:
                print("You don't have enough credit to make this transfer")
                continue

        else:
            print(account_error)
            continue

        print(f'Your new balance: ${main_info[1].balance}')

#Main
users_list = []
generate_user()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ").upper()
    print()

    if userChoice == "1":
        find_user()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missing_email()
    elif userChoice == "4":
        bank_details()
    elif userChoice == "5":
        transfer()
    print()