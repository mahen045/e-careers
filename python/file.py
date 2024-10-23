# fp = open('sample\data.txt', 'r')
# #print(fp.read())
# fp.close()

# fp1=open(r'sample\file1.txt', 'w')
# fp1.write('Sample file in python')
# fp1.close()

# with open(r'sample\data.txt','a') as fp:
#     fp.write("This will go last")

#Write a Python code to read first 2 lines of a file    
# N=2
# with open(r'sample\data.txt','r') as fp:
#     for i in range(N):
#         line = next(fp).strip()
#         print(line)

# with open(r'sample\data.txt', "r") as fp:
#     lines = fp.readlines()
#     print(lines)        

#Write a Python program to write a list content to a file.

# list = ['Red', 'Green', 'Yellow']
# with open(r'sample\dummy1.txt', "w") as fp:
#     for item in list:
#         fp.write("%s\n" % item)
# print('File written successfully')

#Write a python program to combine each line from first file with the 
#corresponding line in second file
with open(r'sample\data.txt') as file1, open(r'sample\dummy.txt') as file2:
    for line1, line2 in zip(file1, file2):
        print(line1+''+line2)