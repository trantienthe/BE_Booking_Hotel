from rest_framework import serializers
from e_be_booking_hotel.models import OrderDetail

class OrderDetailSerializer(serializers.ModelSerializer):
    room_id = serializers.IntegerField(source='room.room_id', read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['id', 'room', 'room_id','order_id', 'price', 'checkin_date', 'checkout_date']  # Include room_id in the fields
