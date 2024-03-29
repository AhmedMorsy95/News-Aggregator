from api import api
import requests
from news import news


class redditAPI(api):
    articles_limit: int = 2
    access_token: str

    def __init__(self):
        self.authorize()

    def authorize(self):
        # in order to use reddit API, developer must first login to acquire an access token.
        url: str = 'https://www.reddit.com/api/v1/access_token'
        client_auth = requests.auth.HTTPBasicAuth('K7DpdijP_n1gog', 'RmI_VxVkHGnGwtUTRVNOnF4YSw4')
        params = {'grant_type': 'password', 'username': 'ahmed-morsy21', 'password': 'ahmed-morsy21'}
        headers = {"User-Agent": "Chrome/77"}
        response = requests.post(url, data=params, auth=client_auth, headers=headers)
        self.access_token = response.json()['access_token']

    # returns only the wanted fields from the dictionary
    def clean_data(self, data: list) -> list:
        cleaned_data: list = []
        for datum in data:
            # only extract wanted fields from the article details.
            current_article = news(datum['data']['title'], datum['data']['url'], 'reddit')
            cleaned_data.append(current_article)
            if len(cleaned_data) == self.articles_limit:
                break

        return cleaned_data

    def list(self) -> list:
        headers = {"Authorization": "bearer " + self.access_token,
                   "User-Agent": "Chrome/77"}
        response = requests.get("https://oauth.reddit.com/r/news", headers=headers)
        # send articles only to clean_data
        return self.clean_data(response.json()['data']['children'])

    def search(self, topic: str) -> list:
        headers: dict = {"Authorization": "bearer " + self.access_token,
                         "User-Agent": "Chrome/77"}
        params: dict = {"q": topic}
        response = requests.get("https://oauth.reddit.com/search", headers=headers, params=params)
        return self.clean_data(response.json()['data']['children'])
