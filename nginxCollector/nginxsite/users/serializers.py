
from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import PasswordField, TokenObtainSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import validate_email

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'slug', 'app_key', 'created_at', 'last_login', "api_identify", "authorization_field"]

        read_only_fields = ['slug', 'email', 'password']
        extra_kwargs = {
            'authorization_field': {'write_only': True},
            'api_identify': {'write_only': True}
        }

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        # try:
        #     user.set_password(validated_data['password'])
        #     user.save()
        # except KeyError:
        #     pass
        return user



class UserCreateSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()

    password = serializers.CharField(write_only=True, required=True, style={
        "input_type": "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2"
        ]
        extra_kwargs = {"password": {"write_only": True}}
        

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

class ApiAndAuthorizationSerializer(serializers.ModelSerializer):
    api_identify = serializers.CharField(required=True)
    authorization_field = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = [
            "authorization_field",
            "api_identify"
        ]
        

class CustomTokenObtainSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass
        self.user = authenticate(**authenticate_kwargs)

        return {}


class CustomTokenObtainPairSerializer(CustomTokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['username'] = str(self.user.username)
        data['slug'] = str(self.user.slug)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
