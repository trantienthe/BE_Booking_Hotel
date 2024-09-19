from rest_framework import viewsets
from ..models import Utilities
from ..serializers import UtilitiesSerializer

class UtilitiesViewSet(viewsets.ModelViewSet):
    queryset = Utilities.objects.all()  # Xác định các đối tượng model mà ViewSet này sẽ làm việc
    serializer_class = UtilitiesSerializer  # Chỉ định serializer sẽ được sử dụng
