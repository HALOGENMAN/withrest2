from rest_framework import serializers
from .models import B

class Bserializers(serializers.ModelSerializer):
    class Meta:
        model = B
        fields = "__all__"