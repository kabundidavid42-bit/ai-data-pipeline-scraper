import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(base_url, headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")
books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one("p.price_color").text
    price = price.replace("Â", "").strip()
    link = book.h3.a["href"]


    books.append({
        "Title": title,
        "Price": price,
        "Link": base_url + link
    })

full_link = base_url + book.h3.a["href"]
df = pd.DataFrame(books)
df.to_csv("books_sample.csv", index=False, encoding="utf-8-sig")
print("CSV saved as books_sample.csv")
