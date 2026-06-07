from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, computed_field

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

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="The ID is not needed on the creation", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=5 ,max_length=200)
    rating: int = Field(gt=0, le=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A novel set in the Roaring Twenties that explores themes of wealth, love, and the American Dream.",
                "rating": 5
            }
        }
    }

books = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel set in the Roaring Twenties that explores themes of wealth, love, and the American Dream.", 5),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "A novel that addresses racial injustice and moral growth in the Deep South during the 1930s.", 5),
    Book(3, "1984", "George Orwell", "A dystopian novel that explores themes of totalitarianism, surveillance, and individuality in a future society.", 4), 
]

@app.get("/books")
async def get_books(): 
    return books 
  
@app.post("/create_book")
# async def create_book(book = Body()):
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book