from django.urls import path, include
from rest_framework import routers

from api.views import ImageViewSet, CreateTokenView

router = routers.DefaultRouter()
router.register("images", ImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", CreateTokenView.as_view(), name="token"),
]

app_name = "api"
