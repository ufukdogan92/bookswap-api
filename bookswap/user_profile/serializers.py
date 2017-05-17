from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

class UserProfileSerializer(serializers.ModelSerializer):
    image=Base64ImageField()
    class Meta:
        model = UserProfile 
        fields = ('user','gender','birthdate','phone','image')

    def create(self, validated_data):
        image=validated_data.pop('image')
        user=validated_data.pop('user')
        gender=validated_data.pop('gender')
        birthdate=validated_data.pop('birthdate')
        phone=validated_data.pop('phone')
        os.remove(image.name)
        return UserProfile.objects.create(user=user,gender=gender, birthdate=birthdate, phone=phone,image=image)

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







