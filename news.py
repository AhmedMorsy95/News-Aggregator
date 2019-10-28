class news:

    def __init__(self, headline: str, link: str, source: str):
        # new fields can be added here.
        self.headline = headline
        self.link = link
        self.source = source

    def display(self):
        print("\t{")
        print("\t\theadline:", self.headline)
        print("\t\tlink:", self.link)
        print("\t\tsource:", self.source)
        print("\t},")
