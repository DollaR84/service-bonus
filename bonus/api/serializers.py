from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Bonus
from .models import Operation


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['balance']


class UserSerializer(serializers.ModelSerializer):
    bonus = BonusSerializer(many=False)
    operations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bonus', 'operations']


class OperationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Operation
        fields = ['user', 'method', 'count', 'desc']
