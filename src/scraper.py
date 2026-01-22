import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_cards = results.find_all("div", class_="card-content")

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=10)
pdf.cell(75, 10, txt="Job title", border = 1, align = "C")
pdf.cell(50, 10, txt="Company", border = 1, align = "C")
pdf.cell(50, 10, txt="Location", border = 1, align = "C")
pdf.cell(15, 10, txt="Links", border = 1, align = "C")
pdf.cell(50, 10, txt = "", ln = 1)

for job_card in python_job_cards:
    pdf.set_font("Arial", size=10)
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    pdf.set_text_color(40,40,255)
    pdf.cell(75, 10, txt = title_element.text.strip(), border = 1, align = "C")
    pdf.set_text_color(40,40,40)
    pdf.set_font("Arial", size=8)
    pdf.cell(50, 10, txt = company_element.text.strip(), border = 1, align = "C")
    pdf.cell(50, 10, txt = location_element.text.strip(), border = 1, align = "C")
    link_url = job_card.find_all("a")[1]["href"]
    pdf.cell(15, 10, txt = "link", link=link_url, border = 1, align = "C")
    pdf.cell(50, 10, txt = "", ln = 1)

pdf.output("JOBS.pdf")