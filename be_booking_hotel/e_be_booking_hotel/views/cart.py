from rest_framework import viewsets, permissions
from e_be_booking_hotel.models import Cart
from e_be_booking_hotel.serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Chỉ cho phép người dùng đã xác thực

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.filter()
