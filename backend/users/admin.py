from django.contrib import admin

from .models import UserAccess, Group


class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'get_users_count')

    def get_users_count(self, obj):
        return obj.users.count()

    get_users_count.short_description = 'Users Count'


admin.site.register(UserAccess, UserAccessAdmin)
admin.site.register(Group, GroupAdmin)