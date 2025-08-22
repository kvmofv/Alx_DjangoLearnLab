from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from .models import CustomUser

class UserRegestrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "profile_picture", "bio", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=50, write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid credentials. ")
        
        token, created = Token.objects.get_or_create(user=user)

        return {
            "user": user,
            "token": token.key
        }
    
class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        
        if user is None:
            raise serializers.ValidationError("Invalid Credentials. ")
        token, created = Token.objects.get_or_create(user=user)
        return {"token": token.key}