# News Aggregator
## Description

This application provides a generic way to aggregate news from different APIs.

The current version aggregates 2 APIs:
1. [Reddit API](https://www.reddit.com/dev/api/)
2. [News API](https://newsapi.org/)

It provides 2 features:
1. List: displays a list of news articles.
2. Search: displays a list of articles about a certain topic.

## Adding a new API
1. Add a new Class for the API which inherits API class and implements the list and search methods as well.
2. Add an instance from the new API to the api_list in newsAggregator Class.
3. Update Unit tests.

## Cloning and running the Project (Ubuntu)
The project comes with a python virtual environment which has all the dependencies.
1. Clone the project.
2. Open the terminal at the project directory.
3. Activate the virtual environment by running

           . venv/bin/activate 

4. Running the server:

            python3 server.py

5. Open the browser and test it!

    http://127.0.0.1:5000/search?q=topic

    http://127.0.0.1:5000/news
