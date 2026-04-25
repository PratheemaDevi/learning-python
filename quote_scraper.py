
import requests
from bs4 import BeautifulSoup
import csv
import os

base_url = "http://quotes.toscrape.com/page/{}/"

file_path = os.path.join(os.getcwd(), "quotes.csv")

with open(file_path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])

    for page in range(1, 4):
        url = base_url.format(page)

        response = requests.get(url)
        response.encoding = response.apparent_encoding  # ✅ Fix encoding

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        for i in range(len(quotes)):
            text = quotes[i].get_text(strip=True)

            # ✅ Clean special characters
            clean_quote = (text
                           .replace("“", "")
                           .replace("”", "")
                           .replace("â€œ", "")
                           .replace("â€", "")
                           .replace("’", "'")
                           )

            writer.writerow([clean_quote, authors[i].text])

print("✅ File saved at:", file_path)