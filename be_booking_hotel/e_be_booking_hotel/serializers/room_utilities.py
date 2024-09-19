from rest_framework import serializers
from ..models import RoomUtilities

class RoomUtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomUtilities
        fields = '__all__'
