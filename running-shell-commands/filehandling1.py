import os
from scriptheader import myheader

myheader("File handling")

# open then write or append contents to file
try:

    # linux / mac doesnt auto create the file
    # os.system("touch ~/Desktop/text.txt")
    
    # open modes: w(write) a(append) r(readonly)
    file1 = open("file1.txt", "a")

    mynewline = input("Enter  line to write to file:")
    file1.write(mynewline + "\n")

except ValueError as ve:
    print(ve)