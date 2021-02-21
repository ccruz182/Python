import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(len(quotes)):
    print('Quote:\t{0}'.format(quotes[i].text))
    print('Author:\t{0}'.format(authors[i].text))
    quote_tags = tags[i].find_all('a', class_='tag')
    #quote_tags_str = ''
    quote_tags_list : list = [qt.text for qt in quote_tags]
    print('Tags:\t{0}\n'.format(quote_tags_list))