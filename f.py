# Книга
class Book:
    title: str
    author: str
    genre: str
    year: int
    pages: int
    
    def __init__(self, title, author, genre, year, pages):
        self.author = author
        self.genre = genre
        self.pages = pages
        self.title = title
        self.year = year
    
    def info(self) -> None:
        print(f"  {self.title}\n  {self.author}\n  genre: {self.genre}\n  {self.year}\n  pages - {self.pages}\n")
        
    def is_long(self) -> bool:
        return (self.pages > 300)

def book_test() -> None:
    book = Book("test", "author", "312", 42, 54)
    book.info()
    book.is_long()

# Студент

# Авто

# Телефон