import csv
import requests
from bs4 import BeautifulSoup
import re

URL = 'http://www.e-himart.co.kr/app/display/showDisplayCategory'

def extract_products(max_page, category):
    product_name = []
    product_price = []
    for page in range(1, max_page + 1):
        result = requests.get(f"{URL}?dispNo={category}#pageCount={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        products_soup = soup.find_all("div", class_="prdInfo")
        price_soup = soup.find_all("div", class_="priceInfo priceBenefit")
        for product in products_soup:
            product_name.append(product.find("p").string)
        for price in price_soup:
            product_price.append(price.find("strong").string)
    return product_name, product_price

def save_to_csv(names, prices):
    file = open("products.csv", mode='w')
    writer = csv.writer(file)
    writer.writerow(['product_name', 'price'])
    for i in range(len(names)):
        writer.writerow([names[i], prices[i]])
    return

def remove_product_code(product_list):
    list_to_return = []
    for name in product_list:
        p = re.sub(r'[()!+_,/]', '', name)
        p = re.sub(r'[A-Z0-9-.]{5,12}', '', p)
        p = re.sub(r'\[[\S\s]+]', '', p)
        p = re.sub(r'\*[\S\s]+\*', '', p)
        list_to_return.append(p)

    return list_to_return

def remove_comma(price_list):
    list_to_return = []
    for price in price_list:
        p = re.sub(r',', '', price)
        p = int(p)
        list_to_return.append(p)

    return list_to_return