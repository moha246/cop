from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from authentication.enums import SignalType
from authentication.signals.senders import email_verification_signal

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = User.get_response_fields() + ("password", "password2")
        extra_kwargs = {
            "is_active": {"read_only": True},
            "is_verified": {"read_only": True},
            "last_login": {"read_only": True},
            "date_joined": {"read_only": True},
            "password": {"write_only": True, "validators": (validate_password,)},
        }

    def create(self, validated_data: dict[str, Any]) -> User:
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User(is_active=False, **validated_data)
        user.set_password(password)
        user.save()
        email_verification_signal.send(User, user=user, signal_type=SignalType.PENDING)
        return user

    def validate_password2(self, password2: str) -> str:
        password = self.initial_data["password"]
        if password2 != password:
            raise serializers.ValidationError("Passwords do not match")
        return password2

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name','last_name','avatar', 'token', 'user_type','phone','organisation','address','designation','dob','gender','current_state']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
