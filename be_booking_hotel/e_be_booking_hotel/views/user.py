from rest_framework import viewsets
from ..models import User
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Xác định các đối tượng model mà ViewSet này sẽ làm việc
    serializer_class = UserSerializer  # Chỉ định serializer sẽ được sử dụng

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)