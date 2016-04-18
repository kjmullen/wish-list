from lists.models import List, ListItem
from rest_framework import serializers
#from userprofiles.serializers import UserSerializer


class ListItemSerializer(serializers.ModelSerializer):

    #user = UserSerializer(read_only=True)
    pledges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ListItem
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):

    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #user = UserSerializer(read_only=True)

    class Meta:
        model = List
        fields = '__all__'
