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


class CreateOrderZaloPayView(APIView):
    @swagger_auto_schema(
        request_body=ZaloPayCreateOrderRequestSerializer,  # Chỉ định serializer request
        responses={200: "Success", 400: "Bad Request", 500: "Server Error"}  # Các mã trả về
    )
    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        total_price = request.data.get('total_price')

        app_id = settings.ZALOPAY_CONFIG["APP_ID"]
        key1 = settings.ZALOPAY_CONFIG["KEY1"]
        endpoint = settings.ZALOPAY_CONFIG["CREATE_ENDPOINT"]

        transID = random.randrange(1000000)
        order = {
            "app_id": app_id,
            "app_trans_id": "{:%y%m%d}_{}".format(datetime.today(), transID),
            "app_user": f"{order_id}",
            "app_time": int(round(time.time() * 1000)),
            "embed_data": json.dumps({'redirecturl': 'http://localhost:3000/'}),
            "item": json.dumps([{}]),
            "amount": total_price,
            "description": "Thanh Toán ZaloPay: ",
            "bank_code": "CC",
            "callback_url": 'https://aef3-183-80-65-28.ngrok-free.app/zalopay-callback/',
        }

        mac_data = f"{order['app_id']}|{order['app_trans_id']}|{order['app_user']}|{order['amount']}|{order['app_time']}|{order['embed_data']}|{order['item']}"
        order["mac"] = hmac.new(key1.encode(), mac_data.encode(), hashlib.sha256).hexdigest()

        try:
            response = requests.post(endpoint, json=order)
            response.raise_for_status()
            response_data = response.json()

            if response_data.get('return_code') != 1:
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            return Response(response_data)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": "Failed to connect to ZaloPay.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
