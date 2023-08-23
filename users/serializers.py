from rest_framework import serializers
from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    # Hash password
    def create(self, validated_data):
        user = UserModel(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
