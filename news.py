class news:
    headline: str
    link: str
    source: str

    def __init__(self, headline: str, link: str, source: str):
        self.headline = headline
        self.link = link
        self.source = source

    def display(self):
        print("headline:", self.headline)
        print("link:", self.link)
        print("source:", self.source)
