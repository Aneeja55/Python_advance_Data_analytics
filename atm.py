bal = 1000
pin = 2314
try_pin = 3
def pincheck():
    global try_pin
    user_pin=int(input("enter pin: "))
    if user_pin==pin:
        return True
    else:
        try_pin-=1
        while try_pin>0:
            print("Incorrect pin, try again")
            user_pin=int(input("enter pin: "))
            if user_pin==pin:
                return True
            else:
                try_pin-=1
        if try_pin==0:
            print("Too many incorrect attempts. Exiting.")
            return False
def withdraw():
    global bal
    amt=int(input("enter amount: "))
    if amt<=bal:
        bal-=amt
        print("Amount "+str(amt)+" withdrawn successfully")
    else:
        print("Insufficient balance")
def enquiry():
    global bal
    print("Your balance is: "+str(bal))
while True:
    option=input("1.Widraw\n2.Enquiry\n3.Exit\nSelect option: ")
    if(option=="1"):
        if pincheck():
            withdraw()
    elif(option=="2"):
        if pincheck():
            enquiry()
    elif(option=="3"):
        break
    else:
        print("Invalid option, please try again")