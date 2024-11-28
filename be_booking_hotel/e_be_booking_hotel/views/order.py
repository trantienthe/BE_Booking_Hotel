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
            # Lấy đối tượng Order
            order = self.get_object()  # Đây sẽ lấy order với ID từ URL
            order.delete()  # Xóa đơn hàng
            return Response(status=status.HTTP_204_NO_CONTENT)  # Trả về 204 No Content khi xóa thành công
        except Order.DoesNotExist:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)  # Trả về lỗi nếu không tìm thấy đơn hàng