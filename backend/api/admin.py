from django.contrib import admin

from.models import Product, Lesson


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'start')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('product', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Lesson, LessonAdmin)