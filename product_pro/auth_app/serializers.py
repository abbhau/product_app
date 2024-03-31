from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','email', 'password2']
    
    def validate(self, attr):
        if attr.get('password') != attr.get('password2'):
            raise serializers.ValidationError("password and password 2 dosent match")
        return attr
    
    def create(self, validated_data):
        validated_data.pop('password2')
        
        return User.objects.create_user(**validated_data)
        

