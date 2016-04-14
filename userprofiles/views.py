from django.shortcuts import render
from lists.models import Pledge
from lists.permissions import IsOwnerOrReadOnly
from lists.serializers import PledgeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from userprofiles.models import UserProfile
from userprofiles.serializers import UserSerializer, UserProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class DetailUser(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUser(generics.ListAPIView):

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


class ListCreatePledge(generics.ListCreateAPIView):

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

