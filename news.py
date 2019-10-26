class news:
    headline: str
    link: str
    source: str

    def __init__(self, headline: str, link: str, source: str):
        self.headline = headline
        self.link = link
        self.source = source

    def display(self):
        print("\t{")
        print("\t\theadline:", self.headline)
        print("\t\tlink:", self.link)
        print("\t\tsource:", self.source)
        print("\t},")
