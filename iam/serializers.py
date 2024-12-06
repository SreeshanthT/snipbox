from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]

    def validate_username(self, value):
        """
        Validate the username to ensure it's unique.
        """
        if User.objects.filter(username=value).exists():
            raise ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        """
        Validate the email to ensure it's unique.
        """
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email already exists.")
        return value

    def validate(self, data):
        """
        Ensure that the password and password_confirm fields match.
        """
        if data["password"] != data["password_confirm"]:
            raise ValidationError({"password_confirm": "Passwords do not match."})
        return data

    def create(self, validated_data):
        """
        Create a new user with the validated data.
        """
        validated_data.pop("password_confirm")  # Remove password_confirm
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.filter(username=data["username"]).first()
        if user and user.check_password(data["password"]):
            return user
        raise serializers.ValidationError("Invalid credentials")


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
