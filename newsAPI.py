from api import api
import requests
from news import news


class newsAPI(api):
    def __init__(self):
        pass

    apiKey: str = 'c23b5e92a669409a89acbb9c2c4362b6'
    url: str = 'https://newsapi.org/v2/everything'
    articles_limit: int = 2

    # returns only the wanted fields from the dictionary
    def clean_data(self, data: dict) -> list:
        cleaned_data: list = []
        for datum in data:
            # extract wanted fields only from the article.
            current_article = news(datum['title'], datum['url'], 'newsapi')
            cleaned_data.append(current_article)
            if len(cleaned_data) == self.articles_limit:
                break

        return cleaned_data

    def list(self) -> list:
        payload = {'apiKey': self.apiKey, 'q': 'news'}
        response = requests.get(self.url, params=payload)
        # send the articles only to clean data
        return self.clean_data(response.json()['articles'])

    def search(self, topic: str) -> list:
        payload = {'apiKey': self.apiKey, 'q': topic}
        response = requests.get(self.url, params=payload)
        return self.clean_data(response.json()['articles'])

