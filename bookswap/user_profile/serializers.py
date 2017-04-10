from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile 
        fields = ('user','gender','birthdate','phone','image')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'first_name', 'last_name',)



class GlobalSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'first_name', 'last_name',)

    def to_native(self, obj):
        if isinstance(obj, User):
            serializer = UserSerializer(obj)
        else:
            raise Exception("Nothing found!")
        return serializer.data


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'first_name', 'last_name',)

    def to_native(self, obj):
        if isinstance(obj, User):
            serializer = UserSerializer(obj)
        else:
            raise Exception("Nothing found!")
        return serializer.data







