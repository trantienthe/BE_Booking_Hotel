from rest_framework import viewsets
from ..models import User
from ..serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Xác định các đối tượng model mà ViewSet này sẽ làm việc
    serializer_class = UserSerializer  # Chỉ định serializer sẽ được sử dụng
