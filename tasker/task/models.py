"""
Models for clickhouse.

Created on 28.05.2021

@author: Ruslan Dolovanyuk

"""

from sqlalchemy import Column

from clickhouse_sqlalchemy import get_declarative_base, engines, types


def get_user_balance_model(metadata):
    Base = get_declarative_base(metadata=metadata)

    class UserBalance(Base):
        __tablename__ = 'user_balance'
        __table_args__ = (
            engines.MergeTree(order_by=['id']),
        )

        id = Column(types.Int32, primary_key=True)
        balance = Column(types.Int32)
        bonus0 = Column(types.Int8)
        bonus1000 = Column(types.Int8)
        bonus100k = Column(types.Int8)
        timestamp = Column(types.DateTime)

    return UserBalance
