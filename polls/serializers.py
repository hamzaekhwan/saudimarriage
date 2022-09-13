from rest_framework import serializers,viewsets
from .models import *


class MarriageContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarriageContract
        fields='__all__'