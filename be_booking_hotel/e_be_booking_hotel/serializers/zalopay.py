from rest_framework import serializers

class ZalopayOrderSerializer(serializers.Serializer):
    app_id = serializers.CharField()
    app_user = serializers.CharField()
    app_trans_id = serializers.CharField()
    app_time = serializers.IntegerField()
    amount = serializers.IntegerField()
    item = serializers.JSONField()
    description = serializers.CharField()
    embed_data = serializers.JSONField()
    callback_url = serializers.URLField(required=False)
    bank_code = serializers.CharField(required=False)

class ZalopayCallbackSerializer(serializers.Serializer):
    data = serializers.CharField()
    mac = serializers.CharField()
    type = serializers.IntegerField()

class ZaloPayCreateOrderRequestSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    total_price = serializers.IntegerField()


