from newsAggregator import newsAggregator
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to News Aggregation App."


@app.route('/news')
def news():
    news_aggregator = newsAggregator()
    news_aggregator.run()
    data: list = []
    for each in news_aggregator.news_list:
        # change the news object to a dictionary so that it can be JSON serializable
        data.append(each.__dict__)
    return jsonify(data)


@app.route('/search')
def search():
    # extract the query field
    topic: str = request.args.get('q')
    news_aggregator = newsAggregator()
    news_aggregator.run(topic)
    data: list = []
    for each in news_aggregator.news_list:
        data.append(each.__dict__)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
