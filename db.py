import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sqlalchemy_utils

SQLITE_DB_PATH = 'styles.db'
SQLITE_URL = f'sqlite:///{SQLITE_DB_PATH}'


class DBConfig():

    STYLE_TABLE_NAME = 'styles'

    def __init__(self, db_url: str):
        self.__engine = None
        self.meta = None
        self.db_url = db_url

    def create_styles_table(self):
        self.meta = MetaData()

        styles = Table(
            self.STYLE_TABLE_NAME,
            self.meta,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('body', String),
        )
        self.meta.create_all(self.__engine)

    def connect(self):
        self.__engine = create_engine(self.db_url, echo=True)

    def styles_table_exists(self) -> bool:
        return self.__engine.dialect.has_table(__engine, self.STYLE_TABLE_NAME)


def get_db_object():
    db_config = DBConfig(SQLITE_URL)
    db_config.connect()
    db_config.create_styles_table()
    return db_config


def init_styles_db():
    return get_db_object()
