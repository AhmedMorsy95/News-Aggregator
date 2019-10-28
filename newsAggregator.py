from newsAPI import newsAPI
from redditAPI import redditAPI
from news import news


class newsAggregator:
    api_list: list = []
    news_list: list = []

    def __init__(self):
        self.api_list.append(newsAPI())
        self.api_list.append(redditAPI())

    def run(self, topic: str = "news"):
        if topic == "news":
            for api in self.api_list:
                api_news_list = api.list()
                for data in api_news_list:
                    self.news_list.append(data)
        else:
            for api in self.api_list:
                api_news_list = api.search(topic)
                for data in api_news_list:
                    self.news_list.append(data)

        self.display_news()

    def display_news(self):
        print("[")
        for data in self.news_list:
            data.display()
        print("]")
