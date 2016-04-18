import os

import stripe
from django.conf import settings
from lists.models import ListItem, List
from rest_framework import serializers
from userprofiles.models import UserProfile, ShippingAddress, Pledge
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    lists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'lists', 'items', 'profile',
                  'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    pledges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = '__all__'


class ListItemSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    pledges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ListItem
        fields = '__all__'


class PledgeSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(read_only=True)
    item = ListItemSerializer(read_only=True)

    class Meta:
        model = Pledge
        fields = ('profile', 'item',  'amount', 'created_at')


class ChargeSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=60)
    item_id = serializers.IntegerField()
    amount = serializers.IntegerField()

    def create(self, validated_data):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        amount = validated_data['amount']
        user = validated_data['user']
        profile = user.profile
        item = validated_data['item_id']
        token = validated_data['token']

        try:
            charge = stripe.Charge.create(
                amount=amount*100,
                currency='usd',
                source=token,
                description="Pledge for item"

            )
            pledge = Pledge.objects.create(profile=profile,
                                           item_id=item,
                                           charge_id=charge['id'],
                                           amount=amount)
            return pledge
        except stripe.error.CardError as e:
            pass

    def update(self, instance, validated_data):
        pass


class ListSerializer(serializers.ModelSerializer):

    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # items = ListItemSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = List
        # fields = '__all__'
        fields = ('id', 'user', 'name', 'expiration_date', 'items',
                  'created_at', 'modified_at', 'expired')