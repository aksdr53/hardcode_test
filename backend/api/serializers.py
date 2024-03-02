from rest_framework import serializers

from .models import Product, Lesson

class ProductSerializer(serializers.ModelSerializer):
    num_lessons = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ('author', 'product_name', 'start', 'price', 'num_lessons')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'video_link')