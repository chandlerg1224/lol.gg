#takes the model that has python related code etc.. and translates the model into a json response.


from rest_framework import serializers
from .models import Room
#id is auto defined in django, code is the room cod
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')