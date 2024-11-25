from rest_framework import viewsets

from e_be_booking_hotel.models import Voucher
from e_be_booking_hotel.serializers import VoucherSerializer


class VoucherViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
