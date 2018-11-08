from django.contrib import admin
from .models import *


# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
