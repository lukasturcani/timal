"""The backend."""

from pathlib import Path
from typing import Literal

from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

app = FastAPI()


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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    """WebSocket endpoint."""
    await websocket.accept()
    while True:
        raw_data = await websocket.receive_bytes()
        print(raw_data)
        data = Message.model_validate_json(raw_data)
        print(data)
