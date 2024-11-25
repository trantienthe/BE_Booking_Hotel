from rest_framework import serializers
from ..models import Room, Hotel, Area, Utilities, RoomImages, RoomUtilities


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = '__all__'

class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField()  # Lồng ghép HotelSerializer
    area = serializers.SerializerMethodField()  # Lồng ghép HotelSerializer
    utilities = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = [
            'room_id',
            'room_type',
            'price_per_night',
            'max_occupancy',
            'description',
            'thumbnail',
            'status',
            'area',
            'hotel',
            'utilities',
            'images'
        ]

    def get_hotel(self, obj):
        return HotelSerializer(obj.area.hotel).data if obj.area and obj.area.hotel else None

    def get_area(self, obj):
        return AreaSerializer(obj.area).data if obj.area else None

    def get_utilities(self, obj):
        # Lấy tất cả tiện ích thông qua bảng RoomUtilities
        utilities = RoomUtilities.objects.filter(room=obj).select_related('utilities')
        return UtilitySerializer([ru.utilities for ru in utilities], many=True).data

    def get_images(self, obj):
        return RoomImagesSerializer(obj.images.all(), many=True).data