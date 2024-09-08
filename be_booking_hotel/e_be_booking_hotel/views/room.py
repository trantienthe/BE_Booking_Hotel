from rest_framework import viewsets
from ..models import Room
from ..serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # Xác định các đối tượng model mà ViewSet này sẽ làm việc
    serializer_class = RoomSerializer  # Chỉ định serializer sẽ được sử dụng
