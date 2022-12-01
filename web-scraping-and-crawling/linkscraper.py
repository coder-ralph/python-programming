from bs4 import BeautifulSoup
import requests

url = "https://www.antiquespride.edu.ph/"

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, "html.parser")

filex = open('antiquespridepagelinks.txt','a')

for link in soup.find_all('a'):
    print(link.get('href'))
    filex.write(str(link.get('href'))+ "\n")

filex.close()
  