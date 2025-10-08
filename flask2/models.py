import db
class Book:
    pk = None
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def create(self):
        db.add_book(self.title, self.author, self.genre)
    
    