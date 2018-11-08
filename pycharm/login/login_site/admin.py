from django.contrib import admin
from . import models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print()
        # 自定义操作
        obj.password = request.POST['password']
        super().save_model(request, obj, form, change)


admin.site.register(models.User, UserAdmin)
