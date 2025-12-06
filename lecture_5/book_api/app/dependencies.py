"""Dependency helpers for FastAPI routes."""

from app.db import SessionLocal


def get_db():
    """
    Create a SQLAlchemy session and yield it to the request handler.
    The session is closed after the request is processed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
