from rest_framework import serializers
from userprofiles.models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    lists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'lists', 'items', 'profile')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    pledges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"
