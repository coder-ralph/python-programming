import wikipedia
from scriptheader import myheader

myheader ("wikiscraper")

searchword = input("enter a key word: ")

# summary = wikipedia.summary(searchword)
# print(summary)

wikicontent = wikipedia.page(searchword).content
print(wikicontent)

try:

    filex = open(searchword + "_data.txt")
    filex.write(wikicontent)
    filex.close()
    print("file created")

except ValueError as ve:
    print(ve)