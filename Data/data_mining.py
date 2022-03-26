import csv
import requests
from bs4 import BeautifulSoup

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


tv_names, tv_prices = extract_products(2, '1011010100')
fridge_names, fridge_prices = extract_products(2, '1011020100')
kimchi_names, kimchi_prices = extract_products(2, '1011050100')
vacuum_names, vacuum_prices = extract_products(1, '1012020100')

names = tv_names + fridge_names + kimchi_names + vacuum_names
prices = tv_prices + fridge_prices + kimchi_prices + vacuum_prices

save_to_csv(names, prices)