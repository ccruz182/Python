import requests
from bs4 import BeautifulSoup


def shopping_scraper(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for product in products:
        product_name = product.find('h4', class_='card-title').find('a').text
        product_price = product.find('h5').text
        print("{0} costs {1}".format(product_name, product_price))

    pages: list = soup.find('ul', class_='pagination').find_all(
        'li', class_='page-item')
    pages.reverse()

    if not pages[0].find('a', class_='page-link'):
        return False

    return pages[0].find('a', class_='page-link')['href']


page_str = '?page=1'
page_counter = 1
while page_str:
    print("*** PAGE {} ***".format(page_counter))
    page_counter += 1
    url = 'https://scrapingclub.com/exercise/list_basic{page}'
    page_str = shopping_scraper(url.format(page=page_str))

print("SCRAPING ENDS")
