from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class UserProfile(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions")

    def __str__(self):
        return self.username


