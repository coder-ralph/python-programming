import os
from scriptheader import myheader

myheader("file reader")

# list all items in a directory
# dir1 = os.listdir("C:\\Users\\ralph\\Music\\python-projects\\")
# for item in dir1:
#    print(item)

# print()
print("choices:")
print("[1] Sample File")
print("[2] Fruits File")
print("[3] PC Names File")

mychoice = input("enter number which to read:")

try:

    if mychoice == "1":
        filetoopen = open("file1.txt","r")
    elif mychoice == "2":
        filetoopen = open("fruits.txt","r")
    elif mychoice == "3":
        filetoopen = open("pcname.csv","r")
    else:
        print("choose between 1-3 only")

    filecontent = filetoopen.read()
    print(filecontent)
    filetoopen.close()

except ValueError as ve:
    print(ve)
