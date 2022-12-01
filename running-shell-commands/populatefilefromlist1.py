import os
from scriptheader import myheader

myheader("samplelist")

try:

    dictionary1 = {'pc1':'henry','pc2':'alvin','pc3':'gomez'}

    pcnames = open("pcname.csv", "a")

    for pc in dictionary1:
        pcnames.write("%s,%s\n" %(pc,dictionary1[pc]))

    print("done")

except ValueError as ve:
    print(ve)