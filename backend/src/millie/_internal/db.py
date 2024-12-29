import sqlite3

from millie._internal.message import AddFile


def add_file(db: sqlite3.Connection, command: AddFile) -> None:
    cursor = db.execute(
        """
        INSERT INTO files (name, path) VALUES (?, ?)
        """,
        (command.name, command.path),
    )
    file_id = cursor.lastrowid
    db.executemany(
        """
        INSERT INTO data (file_id, x, y) VALUES (?, ?, ?)
        """,
        ((file_id, x, y) for x, y in zip(command.xs, command.ys, strict=True)),
    )
    db.commit()


def create_tables(db: sqlite3.Connection) -> None:
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS files
            ( id INTEGER PRIMARY KEY
            , name TEXT NOT NULL
            , path TEXT NOT NULL
            )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS data
            ( id INTEGER PRIMARY KEY
            , file_id INTEGER NOT NULL
            , x REAL NOT NULL
            , y REAL NOT NULL
            , FOREIGN KEY(file_id) REFERENCES files(id)
            )
        """
    )
    db.execute(
        """
        CREATE INDEX IF NOT EXISTS file_id_index
        ON data(file_id)
        """
    )
