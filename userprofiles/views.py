import stripe
from django.shortcuts import render
from lists.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from userprofiles.models import UserProfile, ShippingAddress, Pledge
from userprofiles.permissions import IsAuthenticatedOrWriteOnly
from userprofiles.serializers import UserProfileSerializer,\
    ShippingAddressSerializer, ChargeSerializer, PledgeSerializer, \
    UserSerializer
from rest_framework import generics, status
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


class CreateCharge(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = ChargeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


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