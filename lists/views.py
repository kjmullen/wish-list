from django.shortcuts import render
from lists.models import List, ListItem
from lists.permissions import IsOwnerOrReadOnly
from userprofiles.serializers import ListItemSerializer, ListSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DetailUpdateDeleteListItem(generics.RetrieveUpdateDestroyAPIView):

    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ListCreateListItem(generics.ListCreateAPIView):

    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailUpdateDeleteList(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ListCreateList(generics.ListCreateAPIView):

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListByUser(generics.ListAPIView):

    serializer_class = ListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(user=user).order_by('-created_at')



