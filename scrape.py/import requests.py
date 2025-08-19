import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")
for book in books:
    title = book.h3.a["title"]
    price = book.select_one("p.price_color").text
    rating = book.p["class"][1]  # e.g., 'Three'
    print(f"Title: {title}\nPrice: {price}\nRating: {rating}\n")