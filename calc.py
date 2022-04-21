# imports

# global vars


# functions
def print_menu():
    print("**** PyCalc *****")
    print("-----------")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Division")


def sum(num1,num2):
    result = num1 +num2
    print("The result is:"+str(result))

def subtract(num1,num2):
    result = num1 +num2
    print("The result is:"+ str(result))

def multiply(num1,num2):
    result = num1 +num2
    print("The result is:"+str(result))

    def divide(num1,num2):
    if num2== 0:
    print("Error: Zero dvision is not allowed, are you trying to kill us?")

    else: 
        result = num1 / num2
        print("The result is:"+str(result))




#plain instruction
opt = ""
while opt !="q":
    print_menu()

    opt = input("Please select an option:")
    if opt == "q":
        break # kill the loop

    num1 = float(input("Please provide num1:"))
    num2 = float(input("Please provide num2:"))

    if opt == "1":
        sum(num1 - num2)

    if opt == "2":
        subtract(num1,num2)

    if opt == "3":
        multiply(num1,num2)

    if opt == "4":
    divide(num1, num2)

    print("")
    input("Press Enter to continue...")
    print("\n\n\n")
    
    print("Thank you for using PyCalc!")