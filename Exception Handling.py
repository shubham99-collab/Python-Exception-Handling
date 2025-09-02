# Python program to demonstrate syntax error
# x = 6
# y = 3
# if(x>y):
#     print(x+ "is greater than" +y)

#  Python program to demonstrate exceptions
# x = 9
# y = x/0
# print(y)

# Program 1
# a=int(input("Enter 1st no = "))
# b=int(input("Enter 2nd no = "))
# c=a/b
# print(c) # Do run python in terminal

# Program 3
# try:
#     a=int(input("Enter 1st no = "))
#     b=int(input("Enter IInd no = "))
#     c=a/b
#     print(c)
# except ValueError:
#     print("Error! please input number only.")
# else:
#     print("Thank You....")

# Program 4
# try:
#     saving=5000
#     withdrawl=1000
#     if withdrawl>saving:
#         raise Exception()
#     else: cash=saving-withdrawl
# except Exception:
#     print("Not enough balance!")
# else:
#     print(withdrawl,"has been debited")
#     print("The available balance is :",cash)

# Program 5
# try:
#     fh = open("testfile.txt","w")
#     fh.write("This is exception Handling File")
# except IOError:
#     print("Error! can't write data in file")
# else:
#     print("Written content in the file successfull")

# program 6
# try:
#     fh = open("testfile.txt","r")
#     fh.write("Demo")
# except IOError:
#     print("Error! can't write data in file")
# else:
#     print("Written content in the file successfully")
#    #It shows input-output errors

