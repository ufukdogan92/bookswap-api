from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(UserDetailsSerializer):

    gender = serializers.CharField(source="userprofile.gender", required=False)
    birthdate = serializers.CharField(source="userprofile.birthdate", required=False)
    phone = serializers.CharField(source="userprofile.phone", required=False)
    image = serializers.CharField(source="userprofile.image", required=False)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('gender','birthdate','phone')

    def update(self, instance, validated_data):
        profile_data    = validated_data.pop('userprofile', {})
        gender          = profile_data.get('gender')
        birthdate       = profile_data.get('birthdate')
        phone           = profile_data.get('phone')
        image           = profile_data.get('image')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data:
            if gender:
                profile.gender    = gender
            if birthdate:
                profile.birthdate = birthdate
            if phone:
                profile.phone     = phone
            if image:
                profile.image       = image
            profile.save()
        return instance

