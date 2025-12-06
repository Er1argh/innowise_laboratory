"""Database setup and helper(s)."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLITE_FILE_NAME = 'books.db'
SQLITE_URL = f'sqlite:///{SQLITE_FILE_NAME}'
CONNECT_ARGS = {'check_same_thread': False}

# Engine and session factory used by the application.
engine = create_engine(SQLITE_URL, connect_args=CONNECT_ARGS)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_tables():
    """Create all tables defined in SQLAlchemy models."""
    Base.metadata.create_all(engine)
