from datetime import datetime

from rest_framework import serializers
from e_be_booking_hotel.models import Order, OrderDetail, Room, Cart, Voucher
from .order_detail import OrderDetailSerializer


class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, write_only=True)
    promo_code = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'full_name', 'email', 'phone_number', 'payment_method', 'total_price', 'order_details', 'promo_code', 'voucher', 'status' , 'order_date']

    # Override phương thức create để xử lý việc tạo đơn hàng và các chi tiết đơn hàng
    def create(self, validated_data):
        # Lấy dữ liệu từ validated_data
        order_details_data = validated_data.pop('order_details')  # Dữ liệu OrderDetail
        promo_code = validated_data.pop('promo_code')
        order = Order.objects.create(**validated_data)  # Tạo đối tượng Order

        total_price = 0
        for order_detail_data in order_details_data:
            room = order_detail_data.get('room')
            if room:
                # Lấy checkin_date và checkout_date từ giỏ hàng
                cart_item = Cart.objects.filter(user=validated_data['user'], room=room).first()
                checkin_date = cart_item.checkin_date if cart_item else None
                checkout_date = cart_item.checkout_date if cart_item else None

                # Tính tổng giá cho đơn hàng
                total_price += order_detail_data['price']  # Thêm giá vào tổng

                # Tạo OrderDetail và liên kết với Order
                OrderDetail.objects.create(
                    order=order,
                    room=room,
                    price=order_detail_data['price'],
                    checkin_date=checkin_date,  # Lưu ngày checkin từ giỏ hàng
                    checkout_date=checkout_date  # Lưu ngày checkout từ giỏ hàng
                )

        # Cập nhật tổng giá tiền cho Order
        order.total_price = total_price

        # Nếu voucher tồn tại và hợp lệ, áp dụng voucher cho đơn hàng
        if promo_code:
            try:
                voucher = Voucher.objects.get(code=promo_code, is_active=True)
                # Kiểm tra xem voucher có còn số lượt sử dụng không và có hết hạn không
                voucher_start_date = voucher.start_date.replace(tzinfo=None)
                voucher_end_date = voucher.end_date.replace(tzinfo=None)
                if voucher.usage_count > 0 and voucher_start_date <= datetime.now() <= voucher_end_date:
                    # Tính toán phần trăm giảm giá và trừ vào tổng tiền
                    discount = (total_price * voucher.discount_percentage) / 100
                    order.total_price -= discount
                    order.voucher = voucher

                    # Giảm số lượt sử dụng của voucher
                    voucher.usage_count -= 1
                    voucher.save()
                else:
                    # Nếu voucher không hợp lệ, trả về lỗi
                    raise ValueError("Voucher is expired or has no remaining usage.")
            except Voucher.DoesNotExist:
                raise ValueError("Invalid voucher code.")

        # Lưu thông tin đơn hàng
        order.save()

        # Sau khi tạo đơn hàng thành công, xóa các mục giỏ hàng của người dùng
        user = validated_data['user']
        Cart.objects.filter(user=user).delete()  # Xóa tất cả các mục giỏ hàng của người dùng

        return order
