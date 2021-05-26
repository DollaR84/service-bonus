"""
Service logics for bonus project.

Created on 26.05.2021

@author: Ruslan Dolovanyuk

"""

from .models import Bonus

def add(user, count):
    bonus = Bonus.objects.filter(user=user).first()
    bonus.balance += count
    bonus.save()


def sub(user, count):
    bonus = Bonus.objects.filter(user=user).first()
    bonus.balance -= count
    bonus.save()
