from rest_framework import serializers
from ..models import Utilities

class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = '__all__'
