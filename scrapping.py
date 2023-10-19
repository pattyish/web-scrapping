import requests
import pandas as pd
from bs4 import BeautifulSoup  # Used to scrip website

books = []

for page_numb in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page_numb}.html"
    response = requests.get(url)
    response = response.content
    # Converting content into html format with beautifulSoup
    soup = BeautifulSoup(response, "html.parser")
    # print(soup)
    ol = soup.find("ol")
    articles = ol.find_all("article", class_="product_pod")
    # print(articles)

    for article in articles:
        image = article.find("img")
        title = image.attrs["alt"]
        rating = article.find("p", "star-rating").attrs["class"][1]
        price = article.find("p", "price_color").text[1:]
        price = float(price)
        books.append([title, rating, price])

    # Converting list to data Frame with information scrapped from web
books_dataset = pd.DataFrame(books, columns=[
    "title", "ratwing", "price"])
# Conter data frame into csv file
books_dataset.to_csv("./books.csv")
