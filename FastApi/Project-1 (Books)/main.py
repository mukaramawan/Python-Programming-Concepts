from fastapi import Body, FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

books = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel set in the Roaring Twenties that explores themes of wealth, love, and the American Dream.", 5),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "A novel that addresses racial injustice and moral growth in the Deep South during the 1930s.", 5),
    Book(3, "1984", "George Orwell", "A dystopian novel that explores themes of totalitarianism, surveillance, and individuality in a future society.", 4), 
]

@app.get("/books")
async def get_books():
    return books 

@app.post("/create_book")
async def create_book(book = Body()):
    books.append(book)
    return book