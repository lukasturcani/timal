"""The backend."""

import logging
import sqlite3
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Body, FastAPI
from platformdirs import user_data_path
from rich.logging import RichHandler

from millie._internal import db
from millie._internal.models import AddFile, FileData

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
    db.create_tables(CONNECTION)
    yield


app = FastAPI(lifespan=lifespan)

logger = logging.getLogger(__name__)


@app.post("/add-file")
def add_file(
    data: Annotated[AddFile, Body()],
) -> None:
    db.add_file(CONNECTION, data)


@app.get("/files")
def get_files() -> list[FileData]:
    return list(db.get_files(CONNECTION))
