from fastapi import Body, FastAPI
from pydantic import BaseModel

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
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [

    Book(1, 'Computer Science', 'Intigam G', 'codingWInti', 10),
    Book(2, 'Computer Engineering', 'Samed M', 'codingWSam', 9),
    Book(3, 'Fictional Science', 'Nijat R', 'codingWNij', 8),
    Book(4, 'Design', 'Elshan M', 'codingWEl', 7),
    Book(5, 'Gaming', 'Iltifat G', 'codingWIlti', 6),

]


@app.get("/")
async def all_books():
    return {"message": "Hello world!", "description": "First project on FastAPI"}


@app.post("/create/book")
async def create_book(name, page_count):
    return {"name": name, "page_count": page_count}


# @app.post("/books/create_book")
# async def create_book(book_request: BookRequest):
#     print(type(book_request))
#     new_book = Book(**book_request.model_dump())
#     BOOKS.append(new_book)


# @app.put("/books/{title}")
# async def book_update(title: str, updated_book=BookRequest):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].title.casefold() == title.casefold():
#             BOOKS[i] = updated_book


@app.put("/items/{item_id}")
async def item_detail(item_id):
    return {"item_id": item_id}

@app.delete("/items/{item_id}")
async def item_delete(item_id=None):
    return {"item": item_id}