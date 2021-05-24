from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Bonus


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['balance']


class UserSerializer(serializers.ModelSerializer):
    bonus = BonusSerializer(many=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'bonus']
