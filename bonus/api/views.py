from rest_framework import generics
from django.contrib.auth.models import User

from . import serializers
from .models import Operation

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class OperationList(generics.ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = serializers.OperationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OperationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = serializers.OperationSerializer
