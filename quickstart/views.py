from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# Create your views here.


class UserViewsSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewsSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer