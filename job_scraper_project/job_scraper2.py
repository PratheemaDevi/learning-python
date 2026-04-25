import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.python.org/jobs/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

jobs_container = soup.find("ol", class_="list-recent-jobs")
job_list = jobs_container.find_all("li")

print("Jobs found:", len(job_list))

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Job Title", "Company", "Location", "Link"])

    for job in job_list:
        try:
            title = job.find("h2").text.strip()
            company = job.find("span", class_="listing-company-name").text.strip()
            location = job.find("span", class_="listing-location").text.strip()
            link = "https://www.python.org" + job.find("a")["href"]

            print(title, "|", company, "|", location)
            writer.writerow([title, company, location, link])

        except Exception as e:
            print("Error:", e)


print("✅ Jobs saved successfully")