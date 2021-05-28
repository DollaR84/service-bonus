"""
Special config module for celery.

Created on 27.05.2021

@author: Ruslan Dolovanyuk

"""

from tasker.config import RabbitMQConfig
from tasker.config import RedisConfig


broker_url = f'amqp://{RabbitMQConfig.USER}:{RabbitMQConfig.PASSWORD}@{RabbitMQConfig.HOST}:{RabbitMQConfig.PORT}/{RabbitMQConfig.VHOST}'
result_backend = f'redis://{RedisConfig.HOST}:{RedisConfig.PORT}/{RedisConfig.DBNAME}'
imports = ['tasker.task.tasks']
