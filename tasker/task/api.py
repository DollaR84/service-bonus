"""
API for tasks celery.

Created on 27.05.2021

@author: Ruslan Dolovanyuk

"""

from sqlalchemy import create_engine

from tasker.config import PostgresConfig


def get_users_data():
    db_string = f"postgres://{PostgresConfig.USER}:{PostgresConfig.PASSWORD}@{PostgresConfig.HOST}:{PostgresConfig.PORT}/{PostgresConfig.DBNAME}"
    db = create_engine(db_string)
    with db.connect() as conn:
        query_set = conn.execute("SELECT * FROM api_bonus")
        return {row.id: row.balance for row in query_set}


def set_users_ch(data):
    pass
