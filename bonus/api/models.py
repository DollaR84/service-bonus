from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime

# Create your models here.

class Bonus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bonus')
    balance = models.PositiveIntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_bonus(sender, instance, created, **kwargs):
    if created:
        Bonus.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_bonus(sender, instance, **kwargs):
    instance.bonus.save()


class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operations')
    method = models.CharField(max_length=3, null=False)
    count = models.PositiveIntegerField(null=False)
    desc = models.TextField()
    dt = models.DateTimeField(default=datetime.datetime.now)
