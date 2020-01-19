import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

SQLITE_DB_PATH = 'styles.db'
SQLITE_URL = f'sqlite:///{SQLITE_DB_PATH}'


def sqlite_db_exists() -> bool:
    return os.path.exists(SQLITE_DB_PATH)


def create_styles_db():
    engine = create_engine(SQLITE_URL, echo=True)
    meta = MetaData()

    styles = Table(
        'styles',
        meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('body', String),
    )
    meta.create_all(engine)
    engine.execute(styles.insert().values(name='first', body='###{@}###'))
    engine.execute(styles.insert().values(name='second', body='@@@{@}@@@'))


def init_styles_db():
    if not sqlite_db_exists():
        print(f'sqlite database {SQLITE_DB_PATH} not found. Initializing DB.')
        create_styles_db()
        return
