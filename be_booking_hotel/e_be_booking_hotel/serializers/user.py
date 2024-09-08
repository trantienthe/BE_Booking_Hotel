from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Bạn có thể chỉ định các trường cụ thể nếu không muốn bao gồm tất cả
