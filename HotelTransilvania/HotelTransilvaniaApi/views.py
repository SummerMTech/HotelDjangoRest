from HotelTransilvania.HotelTransilvaniaApi.models import Habitacion
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import generics, serializers, viewsets
from rest_framework import permissions
from HotelTransilvania.HotelTransilvaniaApi.serializers import HabitacionSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HabitacionList(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer 