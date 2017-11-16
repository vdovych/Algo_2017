import urllib.request
import os
import csv

from bs4 import BeautifulSoup

def parse_category(url):
    if not os.path.exists('data'):
        os.makedirs('data')
    html_doc = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    nums = soup.find_all('a', class_='paginator-catalog-l-link')
    num = int(nums[-1].get_text().strip())
    for i in range(num):
       pg = url + 'page={}/'.format(i + 1)
       parse_category_page(pg)

def parse_category_page(url):
    html_doc = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    tiles = soup.find_all("div", class_='g-i-tile-i-title')
    for tile in tiles:
       link = tile.find("a")
       parse_reviews(link['href'] + 'comments/')

def parse_reviews(url):
    html_doc = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    nums = soup.find_all('a', class_='paginator-catalog-l-link')

    if len(nums):
        num = int(nums[-1].get_text().strip())
    else:
        num = 0

    sentiments = []

    for i in range(num):
       pg = url + 'page={}/'.format(i + 1)
       sentiments += parse_reviews_page(pg)

    filename = 'data/' + url.split('/')[4] + '.csv'

    with open(filename,'w') as fl:
        wr = csv.writer(fl, dialect='excel')
        try:
            wr.writerows(sentiments)
        except:
            pass
			
    print(len(sentiments), ' reviews from ', url)


def parse_reviews_page(url):
    html_doc = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    reviews = soup.find_all('article', class_='pp-review-i')
    sentiments = []

    for review in reviews:
        star = review.find('span', class_='g-rating-stars-i')
        text = review.find('div', class_='pp-review-text')
        if star:
            texts = text.find_all('div', class_='pp-review-text-i')
            sentiments.append([star['content'], texts[0].get_text().strip()])

    return sentiments



if __name__ == '__main__':
    url = 'https://rozetka.com.ua/ua/notebooks/c80004/filter/'
    parse_category(url)
