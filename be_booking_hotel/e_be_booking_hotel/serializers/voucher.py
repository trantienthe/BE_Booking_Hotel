from rest_framework import serializers

from e_be_booking_hotel.models import Voucher


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ['voucher_id', 'code', 'discount_percentage', 'start_date', 'end_date', 'is_active','usage_count']
