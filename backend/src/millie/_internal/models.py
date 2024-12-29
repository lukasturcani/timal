from pathlib import Path

from pydantic import BaseModel


class AddFile(BaseModel):
    """Add a file."""

    name: str
    path: Path
    xs: list[float]
    ys: list[float]


class FileData(BaseModel):
    name: str
    path: Path
