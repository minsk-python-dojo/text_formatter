import os

from typing import List

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select
import sqlalchemy_utils

SQLITE_DB_PATH = 'styles.db'
SQLITE_URL = f'sqlite:///{SQLITE_DB_PATH}'


class DBConfig():

    STYLE_TABLE_NAME = 'styles'

    def __init__(self, db_url: str):
        self.__engine = None
        self.meta = None
        self.db_url = db_url
        self.__styles = None

    def create_styles_table(self):
        self.meta = MetaData()
        if not self.styles_table_exists():
            self.__styles = Table(
                self.STYLE_TABLE_NAME,
                self.meta,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('body', String),
            )
            self.meta.create_all(self.__engine)

            conn = self.__engine.connect()
            conn.execute(self.__styles.insert().values(name='hash_border',
                                                       body=''))
            conn.execute(self.__styles.insert().values(name='plain_text',
                                                       body=''))
            conn.execute(self.__styles.insert().values(name='at_sign',
                                                       body=''))
        else:
            self.__styles = Table(
                self.STYLE_TABLE_NAME,
                self.meta,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('body', String),
            )

    def connect(self):
        self.__engine = create_engine(self.db_url, echo=True)

    def styles_table_exists(self) -> bool:
        return self.__engine.dialect.has_table(self.__engine,
                                               self.STYLE_TABLE_NAME)

    def list(self) -> List[str]:
        conn = self.__engine.connect()
        select_query = select([self.__styles])
        styles = conn.execute(select_query)
        all_styles: List[str] = [style.name for style in styles]
        return all_styles


def get_db_object():
    db_config = DBConfig(SQLITE_URL)
    db_config.connect()
    db_config.create_styles_table()
    return db_config


def init_styles_db():
    return get_db_object()
