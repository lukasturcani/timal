"""The backend."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> str:
    """Default root."""
    return "Hello, world!"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> str:
    """Read an item."""
    return f"Item {item_id} {q}"
