from rest_framework import serializers
from ..models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'  # Bạn có thể chỉ định các trường cụ thể nếu không muốn bao gồm tất cả

