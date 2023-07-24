import requests
import time
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    try:
        time.sleep(1)
        result = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if result.status_code == 200:
            return result.text
        else:
            return None
    except requests.ReadTimeout:
        return None


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    list_links = selector.css(".cs-overlay a::attr(href)").getall()
    return list_links


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_link = selector.css(".nav-links .next::attr(href)").get()
    return next_link


def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css('head link[rel="canonical"]::attr(href)').get()
    title = selector.css(".entry-header-inner h1::text").get().strip()
    timestamp = selector.css(".post-meta .meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    reading_time = selector.css(".post-meta .meta-reading-time::text").get()
    sumary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    category = selector.css(".category-style .label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split(" ")[0]),
        "summary": sumary,
        "category": category,
    }


def get_tech_news(amount):
    url_base = "https://blog.betrybe.com/"
    list_links = []
    result_scrape_news = []

    while len(list_links) < amount:
        html_content = fetch(url_base)
        list_links += scrape_updates(html_content)
        url_base = scrape_next_page_link(html_content)

    for new_page in list_links[:amount]:
        html_content = fetch(new_page)
        result_scrape_news.append(scrape_news(html_content))

    create_news(result_scrape_news)
    return result_scrape_news
