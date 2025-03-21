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
        return self.pages > 300

def book_test() -> None:
    book = Book("test", "author", "312", 42, 54)
    book.info()
    book.is_long()

# Студент
class Student:
    name: str
    university: str
    age: int
    year_of_study: int
    gpa: int
    
    def __init__(self, name, age, university, year_of_study, gpa):
        self.age = age
        self.gpa = gpa
        self.name = name
        self.university = university
        self.year_of_study = year_of_study
        
    def study_year(self) -> None:
        print(f"{self.year_of_study}")
        
    def is_excellent(self) -> bool:
        return self.gpa >= 4.5
    
def student_test() -> None:
    student = Student("student", 123, "any", 321, 4.5)
    student.is_excellent()
    student.study_year()

# Авто

# Телефон