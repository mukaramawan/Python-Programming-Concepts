from typing import Optional

from fastapi import Body, FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date=None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(title="The ID is not needed on the creation", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=5 ,max_length=200)
    rating: int = Field(gt=0, le=6)
    published_date: int = Field(ge=1900, le=2030)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A novel set in the Roaring Twenties that explores themes of wealth, love, and the American Dream.",
                "rating": 5,
                "published_date": 1925
            }
        }
    }

books = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel set in the Roaring Twenties that explores themes of wealth, love, and the American Dream.", 5, 1925),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "A novel that addresses racial injustice and moral growth in the Deep South during the 1930s.", 5, 1960),
    Book(3, "1984", "George Orwell", "A dystopian novel that explores themes of totalitarianism, surveillance, and individuality in a future society.", 4, 1948),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books(): 
    return books 
  
@app.post("/create_book", status_code=status.HTTP_201_CREATED)
# async def create_book(book = Body()):
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(ge=0)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
        
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(gt=0, le=6)):
    result = []
    for book in books:
        if book.rating == rating:
            result.append(book)
    return result
 
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(books)):
        if books[i].id == book.id:
            books[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(ge=0)):
    book_changed = False
    for i in range(len(books)):
        if books[i].id == book_id:
            books.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(published_date   : int = Query(ge=1900, le=2030)):
    result = []
    for book in books:
        if book.published_date == published_date:
            result.append(book)
    return result

