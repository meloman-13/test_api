from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the images
        for the currently authenticated user.
        :return: queryset
        """
        user = self.request.user
        return Image.objects.filter(user=user.id)

    def perform_create(self, serializer):
        """
        This method does not allow you to save an image
        with a user other than this session
        :param serializer:
        :return: created object
        """
        serializer.save(user=self.request.user)


class CreateTokenView(ObtainAuthToken):
    """This is the CreateTokenView, what allowed you to login on page and take token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
