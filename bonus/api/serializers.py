from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Bonus
from .models import Operation


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['balance']


class OperationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Operation
        fields = ['user', 'method', 'count', 'desc', 'dt']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['dt'] = instance.dt.strftime('%d.%m.%Y %H:%M:%S')
        return representation


class UserSerializer(serializers.ModelSerializer):
    bonus = BonusSerializer(many=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'bonus']
