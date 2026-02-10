User_database={}
with open("database.csv","r") as f:
    data=f.readlines()
headers=data[0].strip().split(",")
User_database ={h: [] for h in headers}
for line in data[1:]:
    values=line.strip().split(",")
    for key, value in zip(headers,values):
        User_database[key].append(value)
print(User_database)



def write_to_file():
    with open("database.csv", "w") as f:
        f.write(",".join(headers) + "\n")
        for i in range(len(User_database["Name"])):
            f.write(f"{User_database['Name'][i]},{User_database['Password'][i]},{User_database['Status'][i]}\n")
            
def login(name):
    if name in User_database["Name"]:
        index=User_database["Name"].index(name)
        if User_database["Status"][index]=="1":
            print("User already logged in.")
            return False
        try:
            password=input("Enter your password: ")
        except ValueError:
            print("Error reading password.")
            return False
        else:
            if User_database["Password"][index]==password:
                User_database["Status"][index]="1"
                write_to_file()
                return True
            else:
                print("Invalid password.")
                return False
    else:
        print("Name not found")
        return False
    
def logout(name):
    if name in User_database["Name"]:
        index=User_database["Name"].index(name)
        if User_database["Status"][index]=="0":
            print("User already logged out.")
            return False
        else:
            User_database["Status"][index]="0"
            write_to_file()
            return True
    else:
        print("Name not found")
        return False
            
def register():
    try:
        name=input("Enter your name: ")
        if name in User_database["Name"]:
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
            User_database["Name"].append(name)
            User_database["Password"].append(password)
            User_database["Status"].append("0")
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
    
    
