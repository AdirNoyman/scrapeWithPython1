import requests as r
from bs4 import BeautifulSoup
from bs4 import NavigableString


url = 'https://books.toscrape.com/'


res = r.get(url, headers={"Accept": "Application/json"})

soup = BeautifulSoup(res.content, "html.parser")
book_tags = soup.find_all("article", attrs={"class": "product_pod"})
print(len(book_tags))


def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["title"]
    price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
    price = float(price.replace('£', ''))
    rating = book_tag.find(
        "p", attrs={"class": "star-rating"})["class"][-1]

    return {"title": title, "price": price, "rating": rating}


products = [extract_book_data(book_tag) for book_tag in book_tags]
print(products)
