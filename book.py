class Book():
    def __init__(self, title, downloads):
        self.title = title
        self.downloads = int(downloads)

    def __str__(self):
        return f"Title: {self.title}, Downloads: {self.downloads}"