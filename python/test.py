# num1= int(input("Enter first number"))
# num2= int(input("Enter second number"))

# print(num1/2)

# print area of a triangle by taking length of 3 sides as input
# from the user
# to calculate area of triangle use 
# s = (a+b+c)/2
# area = (s(s-a)(s-b)(s-c)) ** 0.5

#Swap two numbers

# x=5
# y=10

# x, y = y, x
# print(x, ' ', y)

#Get the input numbers from the user
#input choice
#1:Add
#2:Subtract
#3:Multiplication
#4:Division
#Based on the choice, do the math and display the result

def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x,y):
    return x/y
print("Please select an operation to perform.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice=input("Enter (1/2/3/4):")
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first Number: "))
            num2 = float(input("Enter second Number: "))
        except ValueError:
            print("Invalid input..Please enter a number")
            continue 
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))   

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        more_calculation = input("wanna do more calculations? (yes/no):") 
        if more_calculation == 'no':
            break    
    else:
        print("Invalid Input")      