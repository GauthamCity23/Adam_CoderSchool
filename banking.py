def bank_start():
    global question
    print('Hello welcome to Adams Bank: ')
    user = input('Please enter your name to get started: ')
    print('Hello ' + user + ' welcome to Americas middest bank')
    username = input("Please enter your username: ")
    password = input("Please enter your password: ") 
    print('Logged in')
    question = input("What do you want to do?\n1) View balance \n2) Deposit \n3) Withdraw \n4) Close account")

def view_balance():
    global balance
    print("Your current balance is: " + str(balance))
    

def deposit():
    global balance 
    amount = int(input("How much would you like to deposit? "))
    balance += amount
    print("Your new balance is: " + str(balance))  

    
def withdraw():
    global balance 
    amount = int(input("How much would you like to withdraw? "))
    if amount > balance:
        print("You do not have enough funds to withdraw that amount.")
    else:
        balance -= amount
        print("Your new balance is: " + str(balance))



def close_account():
    global balance
    if balance > 0:
        print("Please withdraw your remaining balance before closing your account.")
    else:
        print("Your account has been closed. Thank you for banking with us!")



def main():
    bank_start()
    global balance
    balance = 100
    if question == '1':
        view_balance()
    elif question == "2":
        deposit()
    elif question == "3":
        withdraw()
    elif question == "4":
        close_account()
    else:
        print("Please choose 1, 2, 3, or 4")
main()
