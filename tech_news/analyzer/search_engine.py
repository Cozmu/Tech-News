from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    result = search_news({"timestamp": formatted_date.strftime("%d/%m/%Y")})
    return [(news["title"], news["url"]) for news in result]


def search_by_category(category):
    result = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]
