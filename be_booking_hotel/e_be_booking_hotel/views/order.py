# views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from e_be_booking_hotel.serializers import OrderSerializer
from e_be_booking_hotel.models import Order  # Đảm bảo rằng bạn import mô hình Order

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # Đặt queryset cho ModelViewSet
    serializer_class = OrderSerializer  # Đặt serializer class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)  # Lưu dữ liệu
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            order = self.get_object()  # Lấy đối tượng Order
            print(f"Attempting to delete order with ID: {order.id}")  # Debug log
            order.delete()  # Xóa đơn hàng
            return Response(status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            print("Order does not exist")  # Debug log
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
