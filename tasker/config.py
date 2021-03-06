"""
Config module for tasker bonus service.

Created on 26.05.2021

@author: Ruslan Dolovanyuk

"""

import os


class PostgresConfig:
    HOST = os.getenv('PGDBHOST')
    PORT = os.getenv('PGDBPORT')
    DBNAME = os.getenv('PGDBNAME')
    USER = os.getenv('PGDBUSER')
    PASSWORD = os.getenv('PGDBPASSWORD')


class ClickHouseConfig:
    HOST = os.getenv('CHHOST')
    PORT = os.getenv('CHPORT')
    DBNAME = os.getenv('CHDBNAME')
    USER = os.getenv('CHUSER')
    PASSWORD = os.getenv('CHPASSWORD')


class RedisConfig:
    HOST = os.getenv('REDISHOST')
    PORT = os.getenv('REDISPORT')
    DBNAME = os.getenv('REDISDBNAME')


class RabbitMQConfig:
    HOST = os.getenv('RMQHOST')
    PORT = os.getenv('RMQPORT')
    VHOST = os.getenv('RMQVHOST')
    USER = os.getenv('RMQUSER')
    PASSWORD = os.getenv('RMQPASSWORD')
