from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image", "user")
        read_only_fields = ("id",)

        # version from stackoverflow
        # class ImagesBasicUserSerializer(serializers.ModelSerializer):
        #     class Meta:
        #         model = Images
        #         fields = ("image_200",)
        #
        #
        # class ImagesPremiumUserSerializer(serializers.ModelSerializer):
        #     class Meta:
        #         model = Images
        #         fields = (
        #             "image_200",
        #             "image_400",
        #             "image",
        #         )
        #
        #
        # class ImagesEnterpriseUserSerializer(serializers.ModelSerializer):
        #     class Meta:
        #         model = Images
        #         fields = (
        #             "image_200",
        #             "image_400",
        #             "image",
        #         )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "password", "last_name", "username",)
        read_only_fields = ("id", "plan",)
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}

    def create(self, validated_data):
        """Create user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
