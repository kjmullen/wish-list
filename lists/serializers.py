from django.contrib.auth.models import User
from lists.models import List, ListItem, Pledge
from rest_framework import serializers
from userprofiles.serializers import UserProfileSerializer, UserSerializer


class PledgeSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Pledge
        fields = '__all__'


class ListItemSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    pledges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ListItem
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):

    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    user = UserSerializer(read_only=True)

    class Meta:
        model = List
        fields = '__all__'

