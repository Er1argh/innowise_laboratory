"""Books router: CRUD endpoints for the Book model."""

from typing import List, Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.books import Book
from app.schemas.books import BookOut, BookCreate, BookUpdate

router = APIRouter(prefix='/books', tags=['books'])


@router.post('/', response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book.

    The request body is validated and cleaned by Pydantic validators.
    Returns the created Book object (as BookOut).
    """
    new_book = Book(title=book_in.title, author=book_in.author, year=book_in.year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get('/', response_model=List[BookOut])
def get_books(db: Session = Depends(get_db)):
    """Get a list of books."""
    books = db.query(Book).all()
    return books


@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)) -> None:
    """
    Delete a book by id.
    Returns 204 on success, 404 if not found.
    """
    book = db.query(Book).filter_by(id=book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return None


@router.put('/{book_id}', response_model=BookOut)
def update_book(book_id: int, book_in: BookUpdate, db: Session = Depends(get_db)):
    """Partially update a book. Only provided fields are updated."""
    book = db.query(Book).filter_by(id=book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_in.title is not None:
        book.title = book_in.title
    if book_in.author is not None:
        book.author = book_in.author
    if book_in.year is not None:
        book.year = book_in.year

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@router.get('/search/', response_model=List[BookOut])
def search_books(
        title: Annotated[Optional[str], Query()] = None,
        author: Annotated[Optional[str], Query()] = None,
        year: Annotated[Optional[int], Query()] = None,
        db: Session = Depends(get_db)
):
    """
    Search books by title (substring, case-insensitive), author, or exact year.
    Multiple query parameters are combined with AND semantics.
    """
    query = db.query(Book)

    if title is not None:
        query = query.filter(Book.title.ilike(f'%{title}%'))
    if author is not None:
        query = query.filter(Book.author.ilike(f'%{author}%'))
    if year is not None:
        query = query.filter(Book.year == year)

    books = query.all()
    return books
