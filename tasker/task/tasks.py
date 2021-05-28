"""
Tasks celery for bonus service.

Created on 26.05.2021

@author: Ruslan Dolovanyuk

"""

from tasker.celery import app

from tasker.task import api


@app.task
def update():
    data = api.get_users_data()
    api.set_users_ch(data)
