from rest_framework import viewsets

from e_be_booking_hotel.models import Review
from e_be_booking_hotel.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
