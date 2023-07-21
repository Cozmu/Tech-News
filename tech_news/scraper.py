import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        result = requests.get(url, headers={
            "user-agent": "Fake user-agent"}, timeout=3)
        if result.status_code == 200:
            return result.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    list_links = selector.css('.cs-overlay a::attr(href)').getall()
    return list_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
