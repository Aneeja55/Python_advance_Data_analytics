User_database=[]
keys=[]
i=0
with open("database.csv","r") as f:
    data=f.readlines()
    headers=data[0].strip().split(",")
    for line in data[1:]:
        values=line.strip().split(",")
        row_dict={}
        for i, header in enumerate(headers):
            row_dict[header]=values[i]
        User_database.append(row_dict)

def write_to_file():
    with open("database.csv", "w") as f:
        f.write(",".join(headers) + "\n")
        for user in User_database:
            f.write(f"{user['Name']},{user['Password']},{user['Status']}\n")
def login(name):
    for user in User_database:
        if user["Name"]==name:
            if user["Status"]=="1":
                print("User already logged in.")
                return False
            try:
                password=input("Enter your password: ")
            except ValueError:
                print("Error reading password.")
                return False
            else:
                if user["Password"]==password:
                    user["Status"] = "1"
                    write_to_file()
                    return True
                else:
                    print("Invalid password.")
                    return False
    else:
        print("Name not found")
        return False
    
def logout(name):
    for user in User_database:
        if user["Name"]==name:
            if user["Status"]=="0":
                print("User already Logged out.")
                return False
            else:
                user["Status"]="0"
                write_to_file()
                return True
            
def register():
    try:
        name=input("Enter your name: ")
        for user in User_database:
            if user["Name"]==name:
                print("User already exists.")
                return False
    except TypeError:
        print("Error reading input.")
        return False
    else:
        try:
            password=input("Enter your password: ")
        except ValueError:
            print("Error reading input.")
            return False
        else:
            User_database.append({"Name": name, "Password": password, "Status": "0"})
            write_to_file()
            return True

while True:
    print("1.Login\n2.Register\n3.Logout\n4.Exit\n")
    try:
        option=int(input("Select option: "))
    except ValueError:
        print("Invalid input")
        break
    else:
        if(option==1):
            try:
                name=input("Enter your name: ")
            except TypeError:
                print("Type error occurred, please enter a valid input.")
            else:
                if login(name):
                    print("Login successful!")
                    print(f"Welcome, {name}!")
                else:
                    print("Login failed.")
        elif(option==2):
            if register():
                print("Registration successful!")
            else:
                print("Registration failed.")
        elif(option==3):
            try:
                name=input("Enter your name: ")
            except TypeError:
                print("Type error occurred, please enter a valid input.")
            else:
                if logout(name):
                    print("Logout successful!")
        elif(option==4):
            break
        else:
            print("Invalid option, please try again")
    finally: 
        print("Thankyou!")
    
    
