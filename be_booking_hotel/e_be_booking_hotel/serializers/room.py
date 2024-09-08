from rest_framework import serializers
from ..models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # Bạn có thể chỉ định các trường cụ thể nếu không muốn bao gồm tất cả
