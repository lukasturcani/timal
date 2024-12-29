from pathlib import Path
from typing import Literal

from pydantic import BaseModel


class AddFile(BaseModel):
    """Add a file."""

    type: Literal["AddFile"]
    name: str
    path: Path
    xs: list[float]
    ys: list[float]


class Message(BaseModel):
    """A websocket message."""

    command: AddFile
