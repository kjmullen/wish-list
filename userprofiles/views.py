import stripe
from django.shortcuts import render
from lists.models import Pledge
from lists.permissions import IsOwnerOrReadOnly
from lists.serializers import PledgeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from userprofiles.models import UserProfile, ShippingAddress
from userprofiles.permissions import IsAuthenticatedOrWriteOnly
from userprofiles.serializers import UserSerializer, UserProfileSerializer,\
    ShippingAddressSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class DetailUser(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCreateUser(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUserProfile(generics.RetrieveAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ListUserProfile(generics.ListAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DetailUpdateDeletePledge(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ListPledge(generics.ListAPIView):

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

#
# class CreatePledge(generics.CreateAPIView):
#
#     queryset = Pledge.objects.all()
#     serializer_class = PledgeChargeSerializer
#
#     def perform_create(self, serializer):
#         profile = self.request.user.profile
#
#         serializer.save(profile=profile)
#         serializer.save()
#
#
# class CreateCharge(generics.CreateAPIView):
#
#     serializer_class = ChargeSerializer
#
#     def perform_create(self, serializer):
#
#         serializer.save()


class ListCreateShippingAddress(generics.ListCreateAPIView):

    serializer_class = ShippingAddressSerializer
    queryset = ShippingAddress.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)
        serializer.save()

    # TODO:
    # make new Permission IsOwner
    # change permission to only IsOwner


class DetailUpdateDeleteShippingAddress(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShippingAddressSerializer
    queryset = ShippingAddress.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)