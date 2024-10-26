import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL = "https://habr.com/ru/articles/"


def get_article_links():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Не удалось получить доступ к странице")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    matching_articles = []

    for article in articles:
        title_tag = article.find('h2')
        link_tag = article.find('a', class_="tm-article-snippet__title-link")
        date_tag = article.find('time')

        if title_tag and link_tag and date_tag:
            title = title_tag.text.strip()
            date = date_tag.get('datetime').split('T')[0]
            link = link_tag.get('href')
            preview_text = article.text.lower()

            if any(keyword.lower() in preview_text for keyword in KEYWORDS):
                matching_articles.append(f"{date} – {title} – https://habr.com{link}")

    return matching_articles


def get_full_article_text(url):
    response = requests.get(url)
    if response.status_code != 200:
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')
    article_body = soup.find('div', class_="tm-article-body")
    return article_body.text.lower() if article_body else ""


def get_articles_with_keywords():
    articles = get_article_links()
    for article in articles:
        date, title, link = article.split(" – ")
        full_text = get_full_article_text(link)

        if any(keyword.lower() in full_text for keyword in KEYWORDS):
            print(article)


get_articles_with_keywords()
