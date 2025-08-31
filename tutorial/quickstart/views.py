from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import UserSerializers, GroupSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-data_joined')
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]
    