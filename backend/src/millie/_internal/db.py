import sqlite3


def create_tables(db: sqlite3.Connection) -> None:
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS files
            ( id INTEGER PRIMARY KEY
            , name TEXT NOT NULL
            . path TEXT NOT NULL
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
