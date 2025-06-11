from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

#`UserSerializer` ensures that users can register via the API using their username, email, password, and role.
# The password is securely hashed using Django's built-in user creation.

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user