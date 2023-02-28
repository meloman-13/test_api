import os.path
import uuid

from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

from django.db import models
from django.contrib.auth.models import AbstractUser

from test_task import settings
from test_task.settings import ALLOWED_UPLOAD_IMAGES


def image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)

    filename = f"{slugify(instance.user.username)}--{uuid.uuid4()}.{extension}"

    return os.path.join(f"users/images/{instance.user.username}/", filename)


class User(AbstractUser):
    CHOICE_PLAN = [
        ("BASIC", "Basic"),
        ("PREMIUM", "Premium"),
        ("ENTERPRISE", "Enterprise")
    ]
    plan = models.CharField(max_length=255, choices=CHOICE_PLAN, default="Basic")

    def __str__(self):
        return f"{self.username}  {self.plan}"


class Image(models.Model):
    image = models.ImageField(upload_to=image_file_path,
                              validators=[FileExtensionValidator(allowed_extensions=ALLOWED_UPLOAD_IMAGES)], )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="images")


# Variant from stackoverflow
# class Images(models.Model):
#     title = models.CharField(max_length=250)
#     image = models.ImageField(upload_to=user_directory_path)
#     image_200 = models.ImageField(upload_to=user_directory_path_200)
#     image_400 = models.ImageField(upload_to=user_directory_path_200)
#
#
#     def save(self, *args, **kwargs):
#
#
#         super().save(*args, **kwargs)
#
#     img_200 = Image.open(self.image.path)
#     img_400 = Image.open(self.image.path)
#
#     output_size_200 = (200, 200)
#     output_size_400 = (400, 400)
#     img_200.thumbnail(output_size_200)
#     img_400.thumbnail(output_size_400)
#     img_200.save(self.image_200.path)
#     img_400.save(self.image_400.path)
