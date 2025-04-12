from rest_framework import serializers
from .models import Brand, Tea

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tea
        fields = ['id', 'name', 'brand_id', 'range', 'format', 'qty', 'unit', 'price']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['brand'] = representation.pop('brand_id')
        return representation

# MI adta meg a valaszt, hogy ezt igy kell
class TeaSerializer2(serializers.ModelSerializer):
    brand_id = BrandSerializer()

    class Meta:
        model = Tea
        fields = ['id', 'name', 'brand_id', 'range', 'format', 'qty', 'unit', 'price']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['brand'] = representation.pop('brand_id')
        return representation

