from django.urls import path, include
from .views import RoomView

urlpatterns = [
    #url path /api/room returns the roomview as a view
    path("room", RoomView.as_view()),
]