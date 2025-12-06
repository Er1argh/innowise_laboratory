"""SQLAlchemy models for the app (Book)."""

from sqlalchemy import Column, Integer, String

from app.db import Base


class Book(Base):
    """Book model representing the `books` table."""
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    year = Column(Integer, nullable=True)
