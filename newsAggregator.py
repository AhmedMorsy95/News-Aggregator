from newsAPI import newsAPI
from redditAPI import redditAPI


class newsAggregator:

    def __init__(self):
        self.api_list: list = [newsAPI(), redditAPI()]
        self.news_list: list = []

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

    def display_news(self):
        print("[")
        for data in self.news_list:
            data.display()
        print("]")
