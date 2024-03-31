from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['total_prize']

    def create(self, validated_data):
        product = Product(**validated_data)

        ''' To asign the value to the total_prize field
        we have to multiply quantity * prize '''

        product.total_prize = product.quantity * product.prize
        product.save()
        return product
    
    def update(self, instance, validated_data):
        '''to update the instance '''
        instance.name = validated_data.get('name', instance.name)
        instance.prize = validated_data.get('prize', instance.prize)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.total_prize = validated_data.get('total_prize', instance.quantity 
                                                           * instance.prize)
        instance.save()
        return instance

class ProductRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    