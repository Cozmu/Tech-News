from tech_news.database import search_news


def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


def search_by_category(category):
    result = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]
