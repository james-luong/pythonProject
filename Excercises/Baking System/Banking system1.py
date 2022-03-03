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
        print('Name:', self.first_name, self.last_name)
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
            # line[8] = line[8].replace('$','') #remove the dollar sign
            # line[8] = line[8].translate({ord(i): None for i in ','}) #remove the comma
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                 float(line[8][1:]), line[9])

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
            user.display_info()
            count += 1

    print(f'Total: {count} people')

def bank_details():
    count = 0

    for user in users_list:
        count += 1



#Main
users_list = []
generate_user()

for user in users_list:
    user.display_info()