# #str1 = "My name is {firstname}, I am {age}".format(firstname="Mahendra",age=36)
# #str1 = "My name is {0}, I am {1}".format("Mahendra",36)
# str1 = "My name is {}, I am {}".format("Mahendra", 36)
# #print(str1)
from Factors import print_factors
import os
# #Important String function
# str2 = '349eer'
# print(str2.isdigit())

# text = 'pYThon is fun'
# print(text.casefold())

# print(text.split())

# text1 = 'Milk,Chicken,Bread'
# print(text1.rsplit(','))
# print(text1.count('e'))
# print(text1.find('Bread'))

# #Write a python program to get a single string from two given strings
# #separated by space and swap the string.
# #Sample input: 'abc','xyz'
# #Expected output: 'xyz abc'

# string1 = ['hello','world']
# string1.reverse()
# print(" ".join(string1))

# #Write a python program that accepts a filname with extension from the user
# #and prints the extension of the file
# # file = input("Enter file name with extension: ")

# # if '.' not in file:
# #     print("Invalid file name, must contain valid extension type")
# #     exit()

# # else:
# #     file = file.split('.')[1]

# # extension = file.split('.')[0]
# # print(extension)

# file = 'file1.java'  # 0 1 2               # -1 -2 -3
# file = file.rsplit('.')
# print(file[-1])

# #Input an integer n and compute the value of n+nn+nnn
# #example: 5 compute 5+55+555


# #Ask user to enter the list items
# #Ask user to enter a particular number
# #count the number of occurrences of the given number in the list

c = 2+4j
d = 4+7j
#print(c+d)

# Write a python program to turn every item in a list into it's square
# example: [2, 4, 6, 3] Output: [4, 16, 36, 9]

#Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected Output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

numbers = [1, 2, 3, 4, 5]

#odd_nums = []
# for num in numbers:
#     if num % 2 !=0:
#         odd_nums.append(num)
# print(odd_nums)

# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(odd_numbers)

# list1 = ["Hello", "take"]
# list2 = ["Dear", "Sir"]
# result = [txt1 +" "+txt2 for txt1 in list1 for txt2 in list2]
# print(result)
# result = []
# for txt1 in list1:
#     for txt2 in list2:
#         result.append(txt1+txt2)
# print(result)

#List comprehension

# Write a program to find value 20 in the list, 
# and if it is present, replace it with 200.
# Only update the first occurrence of an item.

# Input: list1 = [5, 10, 15, 20, 25, 50, 20]
# Output: [5, 10, 15, 200, 25, 50, 20]

# list1 = [5, 10, 15, 20, 25, 50, 20]
# i = list1.index(20)
# list1[i] = 200
# print(list1)

# tuple1 = (10, 20, 30, 40, 50)

#result = [num for num in list_1 if num != 20]
# tuple1 = tuple1[::-]
# print(tuple1)
# list_2 = []
 
# first_20 = True
 
# for num in list_1:
#     if  num == 20 and first_20 == True:
#         list_2.append(200)
#         first_20 = False
#         print(first_20)
#     else:
#         list_2.append(num)
 
# print(list_2)

#Given a Python list, write a program to remove all occurrences of item 20.


#Reverse the given tuple
# tuple1 = (10, 20, 30, 40, 50)
# Output: (50, 40, 30, 20, 10)

# start
# stop
# step
number_list = [2,4,6,8,10,12]
#print(number_list[::-1])

# Unpack the tuple items
# Input: tuple1 = (10, 20, 30, 40)
# Output:
# print(a) = 10
# print(b) = 20
# print(c) = 30
# print(d) = 40

# Convert two lists into a dictionary
# Input:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

res = dict(zip(keys,values))
print(res)

#Write a Python program to check if value 200 exists in the following dictionary.
#Input:
#    sample_dict = {'a': 100, 'b': 200, 'c': 300}
#Output:
#   200 present in a dict
sample_dict = {'a': 100, 'b': 200, 'c': 300}
print(tuple(sample_dict.keys()))

# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# Output:
#     Math

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict, key=sample_dict.get))

#Enumerate
list1 = ["eat", "drink", "sleep"]

print(dict(enumerate(list1,5)))

print_factors(56)

cwd = os.getcwd()
print(cwd)

directory = "sample"
parent_dir ="C:/Users/user/OneDrive/Documents/E-Careers/sessions/"
path=os.path.join(parent_dir,directory)
os.mkdir(path)
print("Directory created")