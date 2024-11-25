from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from e_be_booking_hotel.models import Cart, User, RoomImages

class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    room_type = serializers.CharField(source='room.room_type', read_only=True)
    room_image = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'room', 'checkin_date', 'checkout_date', 'user_id', 'total_price', 'room_type', 'room_image']

    def get_room_image(self, obj):
        # Trả về URL của thumbnail phòng
        if obj.room.thumbnail:
            return obj.room.thumbnail.url  # Lấy URL từ thumbnail field của Room model
        return None  # Nếu không có thumbnail, trả về None


    def create(self, validated_data):
        # Lấy các trường liên quan từ validated_data để kiểm tra trùng lặp
        user = validated_data.get('user')
        room = validated_data.get('room')

        # Kiểm tra xem mục giỏ hàng đã tồn tại cho người dùng và phòng với cùng ngày hay chưa
        existing_cart_item = Cart.objects.filter(user=user, room=room).first()

        if existing_cart_item:
            raise ValidationError('Phòng này đã có trong giỏ hàng của bạn với cùng ngày.')

        # Tiếp tục tạo mới nếu không tìm thấy trùng lặp
        self.validate_dates(validated_data)

        # Tính tổng giá và chuyển dữ liệu cập nhật sang phương thức create của lớp cha
        return super().create(self.calculate_total_price(validated_data))

    def validate_dates(self, validated_data):
        checkin_date = validated_data.get('checkin_date')
        checkout_date = validated_data.get('checkout_date')

        if checkin_date and checkout_date and checkout_date <= checkin_date:
            raise serializers.ValidationError("Ngày check-out phải sau ngày check-in.")

    def calculate_total_price(self, validated_data):
        checkin_date = validated_data.get('checkin_date')
        checkout_date = validated_data.get('checkout_date')
        room = validated_data.get('room')
        user_id = validated_data['user_id']
        validated_data['user'] = User.objects.get(id=user_id)

        if checkin_date and checkout_date and room:
            total_price = room.price_per_night * (checkout_date - checkin_date).days
            validated_data['total_price'] = total_price

        return validated_data

    def update(self, instance, validated_data):
        # Kiểm tra tính hợp lệ của ngày check-in và check-out
        self.validate_dates(validated_data)

        # Cập nhật ngày check-in và check-out
        instance.checkin_date = validated_data.get('checkin_date', instance.checkin_date)
        instance.checkout_date = validated_data.get('checkout_date', instance.checkout_date)

        # Tính tổng giá mới nếu có thay đổi về ngày
        updated_data = self.calculate_total_price({
            'checkin_date': instance.checkin_date,
            'checkout_date': instance.checkout_date,
            'room': instance.room,
            'user_id': instance.user_id,
        })


        # Cập nhật lại total_price
        instance.total_price = updated_data.get('total_price', instance.total_price)

        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return {"message": "Room removed from cart successfully."}

