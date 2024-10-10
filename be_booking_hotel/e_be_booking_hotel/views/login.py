# views.py
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets, generics

from e_be_booking_hotel.serializers import LoginSerializer


class LoginViewSet(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail:':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
