try:
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    print(f"Name: {name}, Age: {age}")
except ValueError:
    print("Invalid input. Please enter a valid integer as age.")
except TypeError as e:
    print(f"Type error occurred: {e}, please enter a valid input.")
else:
    print("valid Input, no error.")
finally:
    print("Execution completed, Thankyou.")