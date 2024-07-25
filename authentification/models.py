from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    group = models.ManyToManyField(Group, related_name='users', related_query_name='user', blank=True)
    user_permission = models.ManyToManyField(Permission, related_name='users', related_query_name='user', blank=True)