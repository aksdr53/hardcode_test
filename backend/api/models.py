from django.db import models
from django.core.validators import MinValueValidator,

from backend.settings import NAME_MAX_LENGTH

class Product(models.Model):
    author = models.CharField(max_length=NAME_MAX_LENGTH)
    product_name = models.CharField(max_length=NAME_MAX_LENGTH)
    start = models.DateTimeField()
    price = models.IntegerField(validators=[MinValueValidator(1),])


class Lesson(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    video_link = models.URLField()