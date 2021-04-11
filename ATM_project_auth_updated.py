
import random

database = {} # dictionary

# Initializing the system

def init():
    
    import datetime
    now = datetime.datetime.now()
    print("Current date and time:" )
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    print("Welcome to BankPython")
       
    haveAccount = int(input("Do you have account with us: 1 (yes) or 2 (no)? \n" ))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option.")
        init()

# Login

def login():
    
    print("****** Login ******")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")
    
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
              bankOperations()
    
    login()

# Registration

def register():

    print("****** Register ******")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Please create a password for yourself. \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account has been created.")
    print(" == ==== ====== ===== ==== == ")
    print("Your account number is: %d" % accountNumber)
    print("Please make sure you keep it safe.")
    print(" == ==== ====== ===== ==== == ")
    
    login()                

# ATM Bank Operations
        
def bankOperations():
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    print('5. Exit')
   
    selectedOption = int(input('Please select an option:'))
    
    if (selectedOption == 1):
        print('You selected %s' % selectedOption)
        withdrawalOperation()

    elif(selectedOption == 2):
        print('You selected %s' % selectedOption)
        depositOperation()

    elif(selectedOption == 3):
        print('You selected %s' % selectedOption)
        complaintOperation()
    
    elif(selectedOption == 4):
        print('You selected %s' % selectedOption)
        login()
    
    elif(selectedOption == 5):
        print('You selected %s' % selectedOption)
        exit()

    else:
        print('Invalid Option Selected, please try again.')

# Withdrawal 

def withdrawalOperation():

    withdrawalAmount = int(input('How much would you like to withdraw?'))
    print('processing..')
    print('Please take your cash.')
    return withdrawalAmount

# Deposit

def depositOperation():
    
    depositAmount = int(input('How much would you like to deposit?'))
    print('processing..')
    print('Please view your current balance.')
    return depositAmount

# Generate New Random Account Number

def generationAccountNumber():
    
    return random.randrange(1111111111,9999999999)

# Complaint
        
def complaintOperation():
    
    complaint = input('What issue will you like to report?')
    print('Thank you for contacting us.')
    return complaint

# Logout

def logoutOperation():
    login()


# User Dictionary

init()

name = input("What is your name? \n")

allowedUserDictionary = {
    'John':'passwordJohn',
    'Paul':'passwordPaul',
    'Tim':'passwordTim'
    }

if(name in allowedUserDictionary):
    password = input("Your password? \n")    
    
    if(password == allowedUserDictionary[name]):
        print('Welcome %s' % name)
        bankOperations() 
                 
    else:
        print('Password Incorrect, please try again')

else:

    print('Name not found, please try again')


init()
