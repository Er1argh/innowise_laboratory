"""Application entry point."""

from fastapi import FastAPI

from app.routers import books
from app.db import create_tables

app = FastAPI(title='Simple Book Collection API')

# Include routers.
app.include_router(books.router)


def on_startup():
    """Create DB tables on application startup."""
    create_tables()


app.add_event_handler('startup', on_startup)
