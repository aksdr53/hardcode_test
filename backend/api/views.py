from rest_framework import viewsets
from django.db.models import Count
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied

from .models import Product, Lesson
from .serializers import ProductSerializer, LessonSerializer
from users.models import UserAccess

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.annotate(num_lessons=Count('lesson'))
    serializer_class = ProductSerializer


class LessonListByProductView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']

        # Проверка, что пользователь имеет доступ к продукту
        if not UserAccess.objects.filter(user=user, product_id=product_id).exists():
            raise PermissionDenied("You do not have access to this product.")

        # Получение списка уроков для указанного продукта
        return Lesson.objects.filter(product_id=product_id)