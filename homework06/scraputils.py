import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    """
    texts = parser.find_all('a', class_='storylink')
    for text in texts:
        print(text.text)

    points = parser.find_all('span', class_='score')
    for point in points:
        print(point.text)

    authors = parser.find_all('a', class_='hnuser')
    for author in authors:
        print(author.text)

    links = parser.find_all('a', class_='storylink')
    for link in links:
        print(link.get('href'))
    """
    comments = parser.findall('a', class_='href')
    for comment in comments:
        print(comment.text)
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    # PUT YOUR CODE HERE
    return ""


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news
