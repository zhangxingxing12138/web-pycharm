from django.contrib import admin

from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print()
        # 自定义操作
        obj.password = request.POST.get('password')+"haha"
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
