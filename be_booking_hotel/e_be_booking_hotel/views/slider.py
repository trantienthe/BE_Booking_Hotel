from rest_framework import viewsets
from ..models import Slider
from ..serializers import SliderSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()  # Xác định các đối tượng model mà ViewSet này sẽ làm việc
    serializer_class = SliderSerializer  # Chỉ định serializer sẽ được sử dụng
