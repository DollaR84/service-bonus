"""
Tasks celery for bonus service.

Created on 26.05.2021

@author: Ruslan Dolovanyuk

"""

from tasker.celery import app


@app.task
def add(x, y):
    return x + y
