from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, LessonListByProductView

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:product_id>/lessons/', LessonListByProductView.as_view(), name='lesson-list-by-product'),
    path('auth/', include('djoser.urls.authtoken'))
]