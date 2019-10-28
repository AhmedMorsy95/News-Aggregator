from newsAggregator import newsAggregator
from newsAPI import newsAPI
from redditAPI import redditAPI

news_aggregator = newsAggregator()
news_api = newsAPI()
reddit_api = redditAPI()

# tests that news api is returning the  specified number of articles in case of list and search features
def test_news_api():
    articles_list: list = news_api.list()
    if len(articles_list) != news_api.articles_limit:
        print("testing newsAPI list method failed!")
        return False

    articles_list: list = news_api.search("football")
    if len(articles_list) != news_api.articles_limit:
        print("testing newsAPI search method failed!")
        return False

    return True


# tests that reddit api is returning the  specified number of articles in case of list and search features
def test_reddit_api():
    articles_list: list = reddit_api.list()
    if len(articles_list) != reddit_api.articles_limit:
        print("testing redditAPI list method failed!")
        return False

    articles_list: list = reddit_api.search("football")
    if len(articles_list) != reddit_api.articles_limit:
        print("testing redditAPI search method failed!")
        return False

    return True


# tests that aggregator is returning combination of news from both APIs in case of search and list features
def test_news_aggregator() -> bool:
    news_aggregator.run()
    articles_list: list = news_aggregator.news_list
    if len(articles_list) != reddit_api.articles_limit + news_api.articles_limit:
        print("testing newsAggregator list feature failed!")
        return False

    news_aggregator.news_list = []
    news_aggregator.run("football")
    if len(articles_list) != reddit_api.articles_limit + news_api.articles_limit:
        print("testing newsAggregator search feature failed!")
        return False

    return True


def test():
    test1: bool = test_news_api()
    test2: bool = test_reddit_api()
    test3: bool = test_news_aggregator()
    if test1 and test2 and test3:
        print("Passed all tests.")


if __name__ == '__main__':
    test()
