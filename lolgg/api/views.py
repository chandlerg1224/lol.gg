from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.
#view that already is set up to return to us all of the different rooms that are in the database
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() #return all rooms
    serializer_class = RoomSerializer #return all rooms in json format

