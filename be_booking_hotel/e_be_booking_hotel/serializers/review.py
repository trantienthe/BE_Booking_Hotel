from rest_framework import serializers
from e_be_booking_hotel.models import Review, Order, User
from django.core.exceptions import ValidationError

from e_be_booking_hotel.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_id', read_only=True)
    user_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Review
        fields = ['review_id', 'hotel_id', 'user', 'user_id_id', 'rating', 'comment', 'review_date', 'img']

    def validate(self, attrs):
        user_id_id = attrs.get('user_id_id')
        user_id = User.objects.get(pk=user_id_id)
        hotel_id = attrs.get('hotel_id')
        print(attrs)

        if Review.objects.filter(user_id=user_id, hotel_id=hotel_id).exists():
            raise ValidationError("Bạn chỉ được đánh giá một lần cho mỗi khách sạn.")

        if not Order.objects.filter(user_id=user_id, orderdetail__room__area__hotel=hotel_id).exists():
            raise ValidationError("Bạn phải đặt phòng với khách sạn này để gửi đánh giá.")

        return attrs
