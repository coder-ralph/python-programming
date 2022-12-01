from email_scraper import scrape_emails
from bs4 import BeautifulSoup
import requests

url = "https://www.ust.edu.ph/administrative-offices-contact/"

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data,"html.parser")

# print(soup.decode())
gotoemail = scrape_emails(soup.decode())

for eachemail in gotoemail:
    print(eachemail)