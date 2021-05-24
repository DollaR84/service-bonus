from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
