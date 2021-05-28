from rest_framework import generics, permissions

from rest_framework.response import Response

from rest_framework.views import APIView

from django.contrib.auth.models import User

from . import serializers

from .models import Bonus, Operation

from .permissions import IsUser

from . import services

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class BonusBalance(generics.ListAPIView):
    serializer_class = serializers.BonusSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def get_queryset(self):
        return Bonus.objects.filter(user=self.request.user)


class OperationList(generics.ListCreateAPIView):
    serializer_class = serializers.OperationSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def get_queryset(self):
        return Operation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        method = getattr(services, self.request.data['method'])
        method(self.request.user, int(self.request.data['count']))


class OperationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = serializers.OperationSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]
