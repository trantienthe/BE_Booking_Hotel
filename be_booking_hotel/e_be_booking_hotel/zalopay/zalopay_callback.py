import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from e_be_booking_hotel.models import Order


class ZaloPayCallback(APIView):
    def post(self, request):
        result = {}

        try:
            # Lấy thông tin từ callback request
            callback_data_str = request.data.get('data')
            callback_data = json.loads(callback_data_str)
            app_user = callback_data.get("app_user", None)
            order_id = int(app_user)

            # Lấy đơn hàng và cập nhật trạng thái
            order = get_object_or_404(Order, id=order_id)
            order.status = "success"
            order.save()

            result['redirect_url'] = 'http://localhost:3000/registration-success'
            result['return_code'] = 1
            result['return_message'] = 'Payment success'

        except Exception as e:
            result['return_code'] = -1
            result['return_message'] = f"Error: {str(e)}"

        return JsonResponse(result)

