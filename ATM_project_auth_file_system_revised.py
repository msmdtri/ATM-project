# Initializing the system

import random
import os
import validation
import database


def init():
    
    import datetime
    now = datetime.datetime.now()
    print("Current date and time:" )
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    print("Welcome to BankPython")
       
    have_account = int(input("Do you have account with us: 1 (yes) or 2 (no)? \n" ))

    if(have_account == 1):

        login()
    elif(have_account == 2):

        register()
    else:
        print("You have selected invalid option.")
        init()

# Login

def login():

    print("****** Login ******")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = input("What is your password? \n")

        user = database.authenticated_user(account_number_from_user, password)

        user_db_path_1 = 'data/auth_session/'

# Creating a file in auth_session folder to keep track of user login

        try:

            f = open(user_db_path_1+ str(account_number_from_user) + ".txt", "w+")
            f.write(str(user))
            f.close()

        except FileNotFoundError:

            print("User is not found.")

        except FileExistsError:

            print("User does not exist.")

        except TypeError:

            print("Account number invalid: check that you have up to 10 digits and only integers.")

        else:
            bank_operations(user)
            login()

    init()

# Registration

def register():

    print("****** Register ******")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Please create password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your account has been created.")
        print(" == ==== ====== ===== ==== == ")
        print("Your account number is: %d" % account_number)
        print("Please make sure you keep it safe.")
        print(" == ==== ====== ===== ==== == ")
    
        login()

    else:
        print("Something went wrong, please try again.")
        register()

# ATM Bank Operations
        
def bank_operations(user):

    print('Welcome %s %s \n' % (user[0], user[1]))
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    print('5. Exit')
   
    selected_option = int(input('Please select an option:'))
    
    if (selected_option == 1):
        print('You selected %s' % selected_option)
        withdrawal_operation()

    elif(selected_option == 2):
        print('You selected %s' % selected_option)
        deposit_operation()

    elif(selected_option == 3):
        print('You selected %s' % selected_option)
        complaint_operation()
    
    elif(selected_option == 4):
        print('You selected %s' % selected_option)
        logout_operation()
    
    elif(selected_option == 5):
        print('You selected %s' % selected_option)
        exit()

    else:
        print('Invalid Option Selected, please try again.')

# Withdrawal 

def withdrawal_operation():

    account_number_from_user = input("What is your account number? \n")
    withdrawal_amount = float(input('How much would you like to withdraw?'))
    user_db_path = 'data/user_record/'

# Appending withdrawal amount in account balance saved in the user account file

    f = open(user_db_path + str(account_number_from_user) + ".txt", "a+")
    f.write(str(withdrawal_amount))
    f.close()

    print('processing..')
    print('Please take your cash.')
    print('Your current withdrawal amount is {} dollars'.format(withdrawal_amount))
    return withdrawal_amount

# Deposit

def deposit_operation():

    account_number_from_user = input("What is your account number? \n")
    deposit_amount = float(input('How much would you like to deposit?'))
    user_db_path = 'data/user_record/'

# Appending deposit amount in account balance saved in user account file

    f = open(user_db_path + str(account_number_from_user) + ".txt", "a+")
    starting_account_balance = 0
    current_balance = starting_account_balance + deposit_amount
    f.write(str(current_balance))
    f.close()

    print('processing..')
    print('Please view your current balance.')
    print('Your current balance is {} dollars'.format(current_balance))
    return deposit_amount

# Generate New Random Account Number

def generation_account_number():
    
    return random.randrange(1111111111,9999999999)

# Set Current Balance

def set_current_balance(user_details, balance):

    user_details[4] = balance

# Get Current Balance

def get_current_balance(user_details):

    return user_details[4]

# Complaint
        
def complaint_operation():

    account_number_from_user = input("What is your account number? \n")
    complaint = input('What issue will you like to report?')
    user_db_path = 'data/user_record/'

# Appending complaint/notes saved in user account file

    f = open(user_db_path + str(account_number_from_user) + ".txt", "a+")
    f.write(str(complaint))
    f.close()

    print('Thank you for contacting us.')
    return complaint

# Logout

def logout_operation():

    user_account_number = (input("What is your account number? \n"))

    user_db_path_1 = 'data/auth_session/'

# Deleting the file in auth_session folder to indicate that user has logged out of the system

    try:
        os.remove(user_db_path_1 + str(user_account_number) + ".txt")

    except FileNotFoundError:

        print("User is not found.")

    except FileExistsError:

        print("User does not exist.")

    except TypeError:

        print("Invalid account number format.")

    else:
        print("The user has logged out of the system.")
        login()



init()





