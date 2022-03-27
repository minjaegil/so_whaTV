from Data.data_mining import *

tv_names, tv_prices = extract_products(2, '1011010100')
fridge_names, fridge_prices = extract_products(2, '1011020100')
kimchi_names, kimchi_prices = extract_products(2, '1011050100')
vacuum_names, vacuum_prices = extract_products(1, '1012020100')

names = tv_names + fridge_names + kimchi_names + vacuum_names
prices = tv_prices + fridge_prices + kimchi_prices + vacuum_prices

save_to_csv(remove_product_code(names), remove_comma(prices))