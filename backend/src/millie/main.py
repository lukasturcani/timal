"""The backend."""

import logging
import sqlite3
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from platformdirs import user_data_path
from pydantic import BaseModel
from rich.logging import RichHandler

from millie._internal.db import create_tables

DB_PATH = user_data_path("timal", "lukasturcani") / "data.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
CONNECTION = sqlite3.connect(DB_PATH)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:  # noqa: ARG001
    """Lifespan."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            RichHandler(omit_repeated_times=False),
        ],
    )
    create_tables(CONNECTION)
    yield


app = FastAPI(lifespan=lifespan)

logger = logging.getLogger(__name__)


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
    try:
        while True:
            raw_data = await websocket.receive_bytes()
            data = Message.model_validate_json(raw_data)
    except WebSocketDisconnect:
        logger.info("Client disconnected")
