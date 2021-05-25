from rest_framework import generics, permissions
from django.contrib.auth.models import User

from . import serializers

from .models import Operation

from .permissions import IsUser, IsAdmin

from . import services

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


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
