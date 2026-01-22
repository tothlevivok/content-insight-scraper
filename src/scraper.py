import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
print(results.prettify())

job_cards = results.find_all("div", class_="card-content")

for job_card in job_cards:
    print(job_card, end="\n" * 2)