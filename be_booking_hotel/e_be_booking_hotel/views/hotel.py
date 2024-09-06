from rest_framework import viewsets
from ..models import Hotel
from ..serializers import HotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()  # Xác định các đối tượng model mà ViewSet này sẽ làm việc
    serializer_class = HotelSerializer  # Chỉ định serializer sẽ được sử dụng
