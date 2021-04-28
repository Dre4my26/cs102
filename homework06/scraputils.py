import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    news_quantity = 0

    texts = parser.find_all('a', class_='storylink')
    for text in texts:
        news_list.append(text.text)
        news_quantity += 1

    points = parser.find_all('span', class_='score')
    for point in points:
        points_text = point.text
        points_splitted = points_text.split()
        points_total = points_splitted[0]
        news_list.append(points_total)

    authors = parser.find_all('a', class_='hnuser')
    for author in authors:
        news_list.append(author.text)

    links = parser.find_all('a', class_='storylink')
    for link in links:
        news_list.append(link.get('href'))

    comments_filtered = []
    comments = parser.find_all(class_='subtext')
    for comment in comments:
        last = comment.text
        subtext_splitted = last.split()
        if subtext_splitted[-1] == 'discuss':
            comments_filtered.append(0)
        elif subtext_splitted[-1] == 'comment' or subtext_splitted[-1] == 'comments':
            if not isinstance(subtext_splitted[-2:-1], int):
                comments_filtered.append(int(subtext_splitted[-2:-1][0]))
    for comment_points in comments_filtered:
        if isinstance(comment_points, int):
            news_list.append(int(comments_filtered[comment_points]))

    news_list_final = []
    n = 0

    for _ in range(news_quantity):
        news_dict = {'author': news_list[60 + n],
                     'comments': news_list[120 + n],
                     'points': news_list[30 + n],
                     'title': news_list[0 + n],
                     'link': news_list[90 + n]}
        news_list_final.append(news_dict)
        n += 1

    return news_list_final


def extract_next_page(parser):
    """ Extract next page URL """
    next_page_link = parser.find_all('a', class_='morelink')
    next_page_link = next_page_link[0].get('href')
    return next_page_link


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
