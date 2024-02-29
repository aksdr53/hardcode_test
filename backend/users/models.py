from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

from api.models import Product
from backend.settings import NAME_MAX_LENGTH


User = get_user_model()

class UserAcess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    users = models.ManyToManyField(User,
                                   related_name='group')
