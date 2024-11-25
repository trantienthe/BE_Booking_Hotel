import hashlib
import hmac
import json
import random
import time
from datetime import datetime

import requests
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from e_be_booking_hotel.serializers import ZaloPayCreateOrderRequestSerializer
from e_be_booking_hotel.models import Order, Cart, Voucher, OrderDetail, User


class CheckoutZaloPayView(APIView):
    @swagger_auto_schema(
        request_body=ZaloPayCreateOrderRequestSerializer,
        responses={200: "Thành công", 400: "Yêu cầu không hợp lệ", 500: "Lỗi máy chủ"}
    )
    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        total_price = request.data.get('total_price', 0)  # Đảm bảo total_price là kiểu float
        promo_code = request.data.get('promo_code')
        print("Tổng tiền từ yêu cầu:", total_price)

        # Lấy voucher dựa trên mã giảm giá
        voucher = None
        if promo_code:
            try:
                voucher = Voucher.objects.get(code=promo_code)
            except Voucher.DoesNotExist:
                return Response(
                    {"error": "Mã giảm giá không hợp lệ."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        app_id = settings.ZALOPAY_CONFIG["APP_ID"]
        key1 = settings.ZALOPAY_CONFIG["KEY1"]
        endpoint = settings.ZALOPAY_CONFIG["CREATE_ENDPOINT"]

        # Tạo một ID giao dịch ngẫu nhiên
        transID = random.randrange(1000000)
        order = {
            "app_id": app_id,
            "app_trans_id": "{:%y%m%d}_{}".format(datetime.today(), transID),
            "app_user": f"{order_id}",
            "app_time": int(round(time.time() * 1000)),
            "embed_data": json.dumps({'redirecturl': 'http://localhost:3000/'}),  # Địa chỉ URL để chuyển hướng
            "item": json.dumps([{}]),  # Thông tin về các mặt hàng
            "amount": total_price,  # Sử dụng total_price từ yêu cầu
            "description": "Thanh Toán ZaloPay: ",
            "bank_code": "CC",  # Mã ngân hàng (thẻ tín dụng)
            "callback_url": 'https://6726-14-165-105-121.ngrok-free.app/zalopay-callback/',  # URL gọi lại sau khi thanh toán
        }

        # Tính toán MAC (Mã xác thực thông điệp) cho đơn hàng
        mac_data = f"{order['app_id']}|{order['app_trans_id']}|{order['app_user']}|{order['amount']}|{order['app_time']}|{order['embed_data']}|{order['item']}"
        order["mac"] = hmac.new(key1.encode(), mac_data.encode(), hashlib.sha256).hexdigest()

        try:
            user_id = request.data.get('user')  # Lấy user_id từ dữ liệu yêu cầu
            user = User.objects.get(id=user_id)  # Lấy đối tượng User từ cơ sở dữ liệu

            # Tạo đối tượng Order (Đơn hàng)
            order_obj = Order.objects.create(
                user=user,
                full_name=request.data.get('full_name'),
                email=request.data.get('email'),
                phone_number=request.data.get('phone_number'),
                total_price=total_price,  # Sử dụng total_price từ yêu cầu
                payment_method="zalopay",  # Phương thức thanh toán
                status="success",  # Trạng thái đơn hàng
                voucher=voucher,  # Voucher nếu có (dựa trên mã giảm giá)
            )

            # Tạo các đối tượng OrderDetail (Chi tiết đơn hàng) cho mỗi món hàng trong giỏ
            cart_items = Cart.objects.filter(user=user)
            for cart_item in cart_items:
                room = cart_item.room
                room_price = cart_item.room.price_per_night  # Giá phòng theo đêm

                # Tạo đối tượng OrderDetail cho mỗi món hàng trong giỏ
                OrderDetail.objects.create(
                    order=order_obj,  # Liên kết OrderDetail với Order
                    room=room,
                    price=total_price,  # Sử dụng giá phòng cho từng chi tiết đơn hàng
                    checkin_date=cart_item.checkin_date,
                    checkout_date=cart_item.checkout_date,
                )

            # Sau khi tạo chi tiết đơn hàng, cập nhật tổng giá trị đơn hàng
            order_obj.total_price = total_price
            order_obj.save()  # Lưu lại tổng giá trị đơn hàng đã cập nhật

            # Xóa giỏ hàng sau khi xử lý đơn hàng
            Cart.objects.filter(user=user).delete()

            # Gửi yêu cầu tới API ZaloPay
            response = requests.post(endpoint, json=order)
            response.raise_for_status()
            response_data = response.json()

            # Xử lý phản hồi từ ZaloPay
            if response_data.get('return_code') != 1:
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            return Response(response_data)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": "Không thể kết nối với ZaloPay.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        except Exception as e:
            return Response(
                {"error": "Không thể tạo đơn hàng trong hệ thống.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
