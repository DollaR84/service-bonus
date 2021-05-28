"""
App factory module celery for tasker bonus service.

Created on 27.05.2021

@author: Ruslan Dolovanyuk

"""

from __future__ import absolute_import

from celery import Celery

from kombu import Queue, Exchange


def make_app():
    app = Celery('tasker')
    app.config_from_object('tasker.celeryconfig')

    default_exchange = Exchange('default', type='direct')
    web_exchange = Exchange('task', type='direct')

    app.conf.task_default_queue = 'default'
    app.conf.task_default_exchange = 'default'
    app.conf.task_default_routing_key = 'default'

    app.conf.task_queues = (
        Queue('default', default_exchange, routing_key='default'),
        Queue('high_queue', web_exchange, routing_key='high_task'),
        Queue('low_queue', web_exchange, routing_key='low_task'),
    )

    return app
