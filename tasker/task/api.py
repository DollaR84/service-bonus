"""
API for tasks celery.

Created on 27.05.2021

@author: Ruslan Dolovanyuk

"""

import datetime

from sqlalchemy import create_engine, MetaData

from clickhouse_sqlalchemy import make_session

from tasker.config import PostgresConfig, ClickHouseConfig

from tasker.task.models import get_user_balance_model


def get_users_data():
    db_string = f"postgres://{PostgresConfig.USER}:{PostgresConfig.PASSWORD}@{PostgresConfig.HOST}:{PostgresConfig.PORT}/{PostgresConfig.DBNAME}"
    db = create_engine(db_string)
    with db.connect() as conn:
        query_set = conn.execute("SELECT * FROM api_bonus")
        return {row.id: row.balance for row in query_set}


def set_users_ch(data):
    db_string = f"clickhouse+native://{ClickHouseConfig.USER}:@{ClickHouseConfig.HOST}:{ClickHouseConfig.PORT}/{ClickHouseConfig.DBNAME}"
    db = create_engine(db_string)
    session = make_session(db)
    metadata = MetaData(bind=db)
    UserBalance = get_user_balance_model(metadata)

    for user_id, balance in data.items():
        b0 = b1000 = b100k = 0
        if 0 == balance:
            b0 = 1
        elif 1000 <= balance:
            b1000 = 1
        elif 100000 <= balance:
            b100k = 1
        row = UserBalance(id=user_id, balance=balance, bonus0=b0, bonus1000=b1000, bonus100k=b100k, timestamp=datetime.datetime.now())
        session.add(row)
    session.commit()
