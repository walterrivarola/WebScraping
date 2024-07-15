import requests
from bs4 import BeautifulSoup

def scrape_products_by_category(category):
    base_url = f'https://bebemundo.com.py/categoria-producto/{category}'
    products = []

    page_number = 1
    while True:
        page_url = f'{base_url}/page/{page_number}/'
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products_items = soup.find_all('li', class_='product')
            #print(products_items)

            if not products_items:
                break
            print(f'ESTOY EN LA PÁGINA NRO: {page_number}')

            for product in products_items:
                name_element = product.find('h2', class_='woocommerce-loop-product__title')
                price_element = product.find('span', class_='woocommerce-Price-amount')
                if name_element and price_element:
                    name = name_element.get_text(strip=True)
                    price = int(price_element.get_text(strip=True).replace('₲','').replace('.',''))
                    products.append({
                        'name': name,
                        'category': category,
                        'price': price,
                        'page': page_number
                    })
                else:
                    print(f'NO SE ENCONTRARON MÁS PRODUCTOS EN LA PÁGINA {page_number},'
                          f'EN LA CATEGORÍA {category}')

            next_page = soup.find('ul', class_='page-numbers')
            if not next_page:
                break

            page_number += 1
        else:
            break
    return products