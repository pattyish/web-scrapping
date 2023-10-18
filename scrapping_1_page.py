import requests
import pandas as pd
from bs4 import BeautifulSoup  # Used to scrip website

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)
response = response.content

# Converting content into html format with beautifulSoup
soup = BeautifulSoup(response, "html.parser")
# print(soup)
ol = soup.find("ol")
articles = ol.find_all("article", class_="product_pod")
# print(articles)
books = []
for article in articles:
    image = article.find("img")
    title = image.attrs["alt"]
    rating = article.find("p", "star-rating").attrs["class"][1]
    price = article.find("p", "price_color").text[1:]
    price = float(price)
    books.append([title, rating, price])
    # print(price)
# Converting list to data Frame with information scrapped from web
books_dataset = pd.DataFrame(books, columns=["title", "ratwing", "price"])
print(books_dataset)
