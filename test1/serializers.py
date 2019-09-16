from rest_framework import serializers
from .models import A

class ASerializers(serializers.ModelSerializer):
    class Meta:
        model = A
        fields = "__all__"