import random

name=input("Name on your bank account? ")
acno=float(input("Enter Your Account Number: "))
openBal=random.randint(0,100000)
currBal=openBal

def printMenu():
    print(name,"Welcome, i.am.pss")
    print("")
    print("I'll be helping you through the whole experience of using 'Account Manager' ^_^.")
    print("")
    print("Enter 'b'(balance), 'd'(deposit), 'w'(withdraw), or'q'(quit)")

def getTransaction():
    transaction=str(input("What would you like to do? "))
    return transaction

def withdraw(bal,amt):
    global b
    b=bal-amt
    if b<0:
        b=b-10

def formatCurrency(amt):
    return "$%.2f" %amt

###MAIN PROGRAM###

printMenu()
command=str(getTransaction())

while command!="q":
    if (command=="b"):
        print(name,"Your current balance is",formatCurrency(currBal))
        printMenu()
        command=str(getTransaction())
    elif (command=="d"):
        amount=float(input("Amount to deposit?: "))
        currBal=currBal+amount
        print("Current Balance After Depositing: ",currBal)
        printMenu()
        command=str(getTransaction())
    elif (command=="w"):
        amount=float(input("Amount to withdraw? "))
        if currBal>=amount: 
            currBal-=amount 
            print("\n You Withdrew:", amount)
            print("\n Your Currnent Balance:", currBal) 
        else: 
            print("\n Insufficient balance  ") 
  
        
        printMenu()
        command=str(getTransaction())
    else:
        print("Incorrect command. Please try again.")
        printMenu()
        command=str(getTransaction())

print(name,"Goodbye! See you again soon")