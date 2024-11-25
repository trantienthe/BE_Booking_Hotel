from rest_framework import viewsets

from e_be_booking_hotel.models import OrderDetail
from e_be_booking_hotel.serializers import OrderDetailSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
