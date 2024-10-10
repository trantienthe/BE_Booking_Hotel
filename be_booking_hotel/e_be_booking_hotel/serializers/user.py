from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email đã tồn tại.")
        return value

    def create(self, validated_data):
        # Tạo username từ first_name và last_name
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        # Kết hợp first_name và last_name để tạo username
        username = f"{first_name.lower()} {last_name.lower()}"

        # Mã hóa mật khẩu trước khi lưu
        validated_data['password'] = make_password(validated_data['password'])

        # Tạo user và lưu vào DB
        user = User(username=username, **validated_data)  # Tạo user với username
        user.save()

        return user
