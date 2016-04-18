import os

import stripe
from django.conf import settings
from lists.models import Pledge
from rest_framework import serializers
from userprofiles.models import UserProfile, ShippingAddress
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


class ChargeSerializer(serializers.Serializer):

    stripe_token = serializers.CharField(max_length=40)
    amount = serializers.IntegerField()

    def create(self, validated_data):

        stripe.api_key = os.environ('STRIPE_SECRET_KEY')

        try:
            charge = stripe.Charge.create(
                amount=self.amount,
                currency='usd',
                source=validated_data['token'],
                description="Pledge on a wish list item."
            )
            charge_dict = {"charge_id": charge['id'], "amount": charge['amount']}
            return charge_dict

        except stripe.error.CardError:
            pass


    def update(self, instance, validated_data):
        pass


class PledgeChargeSerializer(serializers.ModelSerializer):
    charge_id = ChargeSerializer()
    profile = UserProfileSerializer()

    def create(self, validated_data):
        return stripe.Charge(**validated_data)

    def update(self, instance, validated_data):
        instance.item_id = validated_data.get('item_id', instance.item_id)
        return instance

