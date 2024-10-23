# try:
#     number = int(input('Enter a number '))
#     result = 10/number
#     print(result)
# except ZeroDivisionError:
#     print('Division by zero is not possible')
# except ValueError:
#     print('Please enter a number only')    
# finally:
#     print('Finally block') 
# print('Program continues...')
# 
# class InvalidAgeException(Exception):
#     "This will be raised when the input value is less than 18"

# number = 18
# try:
#     input_num = int(input("Enter a number: "))  
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Valid number")
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")

#Write a python program that executes an operation on a list
# and handles an IndexError exception if the index is out of range    

# list = [1, 2, 3, 4, 5]
# indexChoice = int(input('Enter a number: '))
# try:
#     print(list[indexChoice])
# except IndexError:
#     print('Index out of range!')

# Write a python program that prompts the user to input
# two numbers and raises a TypeError exception if 
# the inputs ar not numerical 

# try:
#     number1 = int(input('Enter a number: '))
#     number2 = int(input('Enter another number: '))
#     result = number1 / number2
#     print(result)
# except ZeroDivisionError:
#     print('You cannot divide by zero!')
# except ValueError:
#     print('Invalid input! Please make sure to only input numbers.')

# Create a user defined exception for MinimumSalaryException
# Get the Employee details like name, dept and salary from the user
# raise MinimumSalaryException if the salary is less than 10,000
# If it it more than 10,000 then show all the details of the employee  
# 
class MinimumSalaryException(Exception):
    "Salary should not be less than 10000"

name = input('Enter emp name: ') 
dept = input('Enter emp department: ') 
salary = int(input('Enter emp salary: '))
try:
    if(salary < 10000):
        raise MinimumSalaryException
    else:
        print('Employee name: '+name)
        print('Employee dept: '+dept)
        print('Employee salary: ',salary)
except MinimumSalaryException:
    print('Salary is less than 10,000')        