from .models import Offer
from rest_framework import serializers

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class OfferSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def to_native(self, obj):
        if isinstance(obj, Offer):
            serializer = OfferSerializer(obj)
        else:
            raise Exception("Nothing found!")
        return serializer.data