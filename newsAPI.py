from api import api
import requests
from news import news


class newsAPI(api):
    def __init__(self):
        pass

    apiKey: str = 'c23b5e92a669409a89acbb9c2c4362b6'
    url: str = 'https://newsapi.org/v2/everything'
    limit: int = 2

    # returns only the wanted fields from the dictionary
    def clean_data(self, data: dict) -> list:
        cleaned_data: list = []
        for datum in data:
            cleaned_data.append(news(datum['title'], datum['url'], 'newsapi'))
            if len(cleaned_data) == self.limit:
                break

        return cleaned_data

    def list(self) -> list:
        payload = {'apiKey': self.apiKey, 'q': 'news'}
        response = requests.get(self.url, params=payload)
        return self.clean_data(response.json()['articles'])

    def search(self, topic: str) -> list:
        payload = {'apiKey': self.apiKey, 'q': topic}
        response = requests.get(self.url, params=payload)
        return self.clean_data(response.json()['articles'])

