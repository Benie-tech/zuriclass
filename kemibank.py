import datetime
import random

now = datetime.datetime.now()
print("Current date and time = %s" % now)
print("Today's date:  = %s/%s/%s" % (now.day, now.month, now.year))
print("The current time is : = %s:%s:%s" % (now.hour, now.minute, now.second))

database = {}

def init():
    print("Welcome to kemibank")

    Accountdetail = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if (Accountdetail == 1):

        login()
    elif (Accountdetail == 2):

        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    print("***** Login ****")

    accountnumberUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountnumber, userdetail in database.items():
        if (accountnumber == accountnumberUser):
            if (userdetail[3] == password):
                bankoperation(userdetail)


    login()


def register():
    print("***** Register ****")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("create a password for yourself \n")

    accountnumber = generateaccountnumber()

    database[accountnumber] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== =====")
    print("Your account number is: %d" % accountnumber)
    print("Thank you for choosing kemibank")
    print(" == ==== ====== ===== ===")

    login()


def bankoperation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    Options = int(input("What would you like to do? (1) deposit\n (2) withdrawal\n (3) complaint\n (4) logout\n "))

    if (Options == 1):
        depositOperation()

    elif (Options == 2):
        withdrawalOperation()

    elif (Options == 3):
        complaintOperation()

    elif (Options == 4):
        logout()
    else:

        print("Invalid option selected")
        bankoperation(user)

#d=deposit
def depositOperation():
    print("You selected option 1")
    d = int(input('How much do you want to deposit?'))
    print("your current balance is")

#w=withdrawal
def withdrawalOperation():
     print("You selected option 2")
     w = int(input('How much do you want to withdraw?'))
     print("Please take your cash")

def complaintOperation():
    Print(" You Selected option 3")
    print(" == ==== ====== =====")
    print('Please, type in your complains below')

def logoutOperation():
    Print(" You Selected option 4")
    print(" == ==== ====== =====")
    print('Thank you for banking with Kemibank')


def generateaccountnumber():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()

init()
