from .models import Bonus

def add(user, count):
    bonus = Bonus.objects.filter(user=user).first()
    bonus.balance += count
    bonus.save()


def sub(user, count):
    bonus = Bonus.objects.filter(user=user).first()
    bonus.balance -= count
    bonus.save()
