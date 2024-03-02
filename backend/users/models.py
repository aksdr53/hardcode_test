from django.db import models
from django.contrib.auth import get_user_model

from api.models import Product
from backend.settings import NAME_MAX_LENGTH, MAX_NUMBER


User = get_user_model()

class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.add_to_group()
        super().save(*args, **kwargs)

    def add_to_group(self):
        print('add')
        product_groups = Group.objects.filter(product=self.product)
        print(product_groups)
        
        if product_groups.exists():
            print('exist')
            # Находим группу с минимальным числом участников
            min_group = min(product_groups, key=lambda group: group.users.count())

            # Проверяем, если число пользователей в группе меньше MAX_NUMBER
            if min_group.users.count() < MAX_NUMBER:
                # Добавляем пользователя в выбранную группу
                min_group.users.add(self.user)
            else:
                # Создаем новую группу и добавляем пользователя
                new_group = Group.objects.create(name='New Group', product=self.product)
                new_group.users.add(self.user)
        else:
            print('else')
            # Создаем новую группу, так как группы отсутствуют
            new_group = Group.objects.create(name='New Group', product=self.product)
            new_group.users.add(self.user)


class Group(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    users = models.ManyToManyField(User,
                                   related_name='group')
