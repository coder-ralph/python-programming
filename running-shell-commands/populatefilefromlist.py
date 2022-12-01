import os
from scriptheader import myheader

myheader("samplelist")

try:

    list1 = ["apples", "oranges", "mangoes"]

    myfruits = open("fruits.txt", "a")

    for f in list1:
        myfruits.write(f + "\n")

    print("done")

except ValueError as ve:
    print(ve)