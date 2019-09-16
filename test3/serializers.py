from rest_framework import serializers
from .models import B

class BSerializers(serializers.ModelSerializer):
    class Meta:
        model = B
        fields = "__all__"